from . import Session
from .models import Request


def empty_requests_table():
    session = Session()
    session.query(Request).delete()
    session.commit()


def get_all_requests():
    session = Session()
    return session.query(Request).all()
