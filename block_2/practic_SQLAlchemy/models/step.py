from sqlalchemy import Column, Integer, String
from .base import Base


class Step(Base):
    __tablename__ = 'step'
    step_id = Column(Integer, primary_key=True)
    name_step = Column(String)
