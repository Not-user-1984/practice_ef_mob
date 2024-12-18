from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class Buy(Base):
    __tablename__ = 'buy'
    buy_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'))
    book_id = Column(Integer, ForeignKey('book.book_id'))
    amount = Column(Integer)
