import os

from .models import Request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(os.environ.get('LOGSTAR_DB_URL'))
Session = sessionmaker(bind=engine)


def get_all_requests():
    """
    Get all requests from the Requests table
    """
    session = Session()
    return session.query(Request).all()
