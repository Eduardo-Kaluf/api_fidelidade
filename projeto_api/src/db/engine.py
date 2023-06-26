from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    engine = create_engine("mysql://root:root@127.0.0.1:3306")
    return engine


def get_session():
    Session = sessionmaker(bind=get_engine())
    session = Session()
    return session
