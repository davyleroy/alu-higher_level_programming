#!/usr/bin/python3
"""print state objects from input"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        state_name = sys.argv[4]
        state = session.query(State).filter(State.name == state_name).first()
        if state is None:
            print("Not found")
        else:
            print(f'{state.id}')
