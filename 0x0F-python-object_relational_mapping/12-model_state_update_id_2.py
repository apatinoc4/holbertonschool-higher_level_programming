#!/usr/bin/python3
"""
changes the name of a State object
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
    change = session.query(State).get(2)
    change.name = 'New Mexico'
    session.commit()
    session.close()
