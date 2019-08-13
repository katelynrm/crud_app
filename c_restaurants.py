from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine 

DBSession = sessionmaker(bind=engine)
session = DBSession()

restaurants = [Restaurant(name = "Panda Garden"),
            Restaurant(name = "Tonys Bistro"),
            Restaurant(name = "Andala"),
            Restaurant(name = "Autie Anns Diner"),
            Restaurant(name = "Cocina Y Amor")]

for restaurant in restaurants:
    session.add(restaurant)

session.commit()