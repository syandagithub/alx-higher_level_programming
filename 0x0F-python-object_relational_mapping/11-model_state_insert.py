#!/usr/bin/python3
"""
prints the state object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
    session.close()
