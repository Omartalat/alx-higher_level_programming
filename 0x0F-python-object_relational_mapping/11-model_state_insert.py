#!/usr/bin/python3
"""
Script to add a new State object "Louisiana" to the database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
Prints the new state's id after adding it to the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name='Louisiana')

    session.add(state1)
    session.commit()

    print(state1.id)
