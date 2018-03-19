from sqlalchemy import func
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    # Request fields
    url = Column(String, nullable=False)
    method = Column(String, nullable=False)
    headers = Column(String, nullable=True)
    # TODO: payload

    # Reponse fields
    response_content = Column(String, nullable=True)
    response_status_code = Column(Integer, nullable=True)
    # TODO: add field response headers
    # TODO: add field elapsed time, or have a DateTime field and calculate

    # System fields
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return '{} {}'.format(self.id, self.url)
