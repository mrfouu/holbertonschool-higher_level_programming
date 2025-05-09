#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' in their name from the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
