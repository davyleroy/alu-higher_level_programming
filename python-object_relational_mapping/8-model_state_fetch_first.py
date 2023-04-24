#!/usr/bin/python3
""" lists first state object from the database """


import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    row = session.query(State).first()

    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
    session.close()
