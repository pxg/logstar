import os

from .models import Request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('LOGSTAR_DB_URL'))
Session = sessionmaker(bind=engine)


def get_all_requests():
    """
    Get all requests from the requests table
    """
    return Session().query(Request).all()


def get_highest_request_id():
    """
    Get ID of request with the highest ID from the requests table
    """
    return Session().query(Request).order_by(Request.id.desc()).limit(1).one().id
