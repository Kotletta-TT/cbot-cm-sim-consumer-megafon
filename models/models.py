from sqlalchemy import Column, Integer, String, BigInteger, JSON, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sim(Base):
    __tablename__ = 'simcards'
    id = Column(Integer, primary_key=True)
    id_provider = Column(String(20))
    phone = Column(String(20))
    active = Column(Boolean)
    services = Column(JSON)
    balance = Column(String(15))
    rate = Column(String(50))
    minute_remain = Column(String(10))
    minute_total = Column(String(10))
    accured = Column(String(15))
    subscr_fee = Column(String(15))


    def __init__(self, id, phone, active, services, balance, rate, minute_remain, minute_total, accured, subscr_fee) -> None:
        self.id = id
        self.phone = phone
        self.active = active
        self.balance = balance
        self.services = services
        self.rate = rate
        self.minute_remain = minute_remain
        self.minute_total = minute_total
        self.accured = accured
        self.subscr_fee = subscr_fee