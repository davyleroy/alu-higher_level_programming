#!/usr/bin/python3
""" adds the State object "Louisiana" to the database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
