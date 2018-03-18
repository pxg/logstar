import requests

from sqlalchemy import create_engine, func
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# For Monky Patching
old_boring_post = requests.post
old_boring_get = requests.get

# SQLAlchemy configuration (can we move this? to it's own file?)
# TODO: pick up credentials from envvar
engine = create_engine('postgresql://petegraham@localhost/logstar')
Base = declarative_base()
Session = sessionmaker(bind=engine)


# TODO: move to models.py file
class Request(Base):
    # TODO: specify what fields can be null
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    method = Column(String)
    response_content = Column(String)
    response_status_code = Column(Integer)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    # Column('headers', String),  # Should be JSON?
    # Column('data', String),  # Should be JSON?

    def __repr__(self):
        return '{} {}'.format(self.id, self.url)


# TODO: move this to a initial configuration command
Base.metadata.create_all(engine)


def empty_requests_table():
    session = Session()
    session.query(Request).delete()
    session.commit()


# TODO: move from this file?
def get_all_requests():
    session = Session()
    return session.query(Request).all()


def logstar_on():
    """
    Switch logstar on so it's logs request and response data
    Monkey patch the requests get and post functions
    """
    requests.get = get_and_log
    requests.post = post_and_log


def get_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests get function
    """
    request_instance = log_request('GET', *args, **kwargs)
    session = Session()
    session.add(request_instance)
    session.commit()

    response = old_boring_get(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def post_and_log(*args, **kwargs):
    """
    Log the request and response data and call original requests post function
    """
    request_instance = log_request('POST', *args, **kwargs)
    session = Session()
    session.add(request_instance)
    session.commit()

    response = old_boring_post(*args, **kwargs)

    log_response(request_instance, response)
    session.commit()
    return response


def log_request(method, *args, **kwargs):
    """
    Log the details of the requests
    """
    # TODO: log header - kwargs.get('headers'))
    # TODO: log data - kwargs.get('data')))
    request_instance = Request(url=args[0], method=method)
    return request_instance


def log_response(request_instance, response):
    """
    Log the details of the response
    """
    request_instance.response_content = response.text
    request_instance.response_status_code = response.status_code
    # TODO: save time response.elapsed.total_seconds()))
    # TODO: save headers: {}'.format(response.headers))
