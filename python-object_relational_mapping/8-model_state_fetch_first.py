#!/usr/bin/python3
"""Lists the first State object from the database using SQLAlchemy."""
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

    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
