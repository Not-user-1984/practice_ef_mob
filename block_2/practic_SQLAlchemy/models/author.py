from sqlalchemy import Column, Integer, String
from base import Base


class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)
