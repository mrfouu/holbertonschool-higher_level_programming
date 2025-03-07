#!/usr/bin/python3
"""Updates the name of the State with id 2 to 'New Mexico' in the database."""
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

    update = session.query(State).filter(State.id == 2).first()
    update.name = "New Mexico"
    session.commit()
    session.close()
