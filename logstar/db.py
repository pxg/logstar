"""
TODO: move functions to models.py
"""
from .models import Request
from .database import db_session


def get_all_requests():
    """
    Get all requests from the requests table
    """
    return db_session().query(Request).all()


def get_highest_request_id():
    """
    Get ID of request with the highest ID from the requests table
    """
    return db_session().query(Request).order_by(Request.id.desc()).limit(1).one().id
