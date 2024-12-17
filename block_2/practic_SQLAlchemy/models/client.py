from sqlalchemy import Column, Integer, String
from base import Base


class Client(Base):
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    email = Column(String)
