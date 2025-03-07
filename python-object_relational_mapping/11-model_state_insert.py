#!/usr/bin/python3
"""Adds a new State object with the name 'Louisiana' to the database and prints its id."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
