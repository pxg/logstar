from . import Session
from .models import Request


def get_all_requests():
    session = Session()
    return session.query(Request).all()
