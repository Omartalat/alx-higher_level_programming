#!/usr/bin/python3
"""
a script prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
