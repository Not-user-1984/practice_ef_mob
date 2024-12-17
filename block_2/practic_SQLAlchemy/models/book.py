from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    genre_id = Column(Integer, ForeignKey('genre.genre_id'))
    city_id = Column(Integer, ForeignKey('city.city_id'))
    price = Column(Integer)
    amount = Column(Integer)
