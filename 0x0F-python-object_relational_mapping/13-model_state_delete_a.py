#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import update

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    session = Session(eng)
    session.query(State).filter(State.name.like('%a%')).delete(
            synchronize_session='fetch')
    session.commit()
    session.close()
