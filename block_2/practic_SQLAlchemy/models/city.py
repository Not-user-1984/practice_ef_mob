from sqlalchemy import Column, Integer, String
from base import Base


class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)
