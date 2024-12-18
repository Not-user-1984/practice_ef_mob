from sqlalchemy import Column, Integer, ForeignKey, Date
from .base import Base


class BuyStep(Base):
    __tablename__ = 'buy_step'
    buy_id = Column(Integer, ForeignKey('buy.buy_id'), primary_key=True)
    step_id = Column(Integer, ForeignKey('step.step_id'), primary_key=True)
    date_step_beg = Column(Date)
    date_step_end = Column(Date)
