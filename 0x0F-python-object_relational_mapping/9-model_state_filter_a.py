#!/usr/bin/python3
"""
Find all states with an 'a' in them
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    session = Session(eng)
    for state in session.query(State).filter(
            State.name.like("%a%")).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
