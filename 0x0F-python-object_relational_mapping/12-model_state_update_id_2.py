#!/usr/bin/python3
"""
Script to change the name of a State object in the database hbtn_0e_6_usa
to "New Mexico" where id = 2. Takes 3 arguments: mysql username,
mysql password, and database name.
"""
import sys
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        stmt = (
            update(State)
            .where(State.id == 2)
            .values(name='New Mexico')
        )

        session.execute(stmt)
        session.commit()
    except Exception as e:
        print('Error: {}'.format(e))
        session.rollback()
    finally:
        session.close()
