from sqlalchemy import Column, Integer, Date, DECIMAL

from app.models import Base


class Statistics(Base):
    __tablename__ = 'statistic'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=True)
    views = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    cost = Column(DECIMAL, nullable=True)
    cpc = Column(DECIMAL, nullable=True)
    cpm = Column(DECIMAL, nullable=True)
