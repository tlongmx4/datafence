from sqlalchemy import Column, Integer, String, JSON, Boolean, ForeignKey, DateTime, Float
from db.database import Base
from datetime import datetime

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    aliases = Column(JSON)
    addresses = Column(JSON)
    date_of_birth = Column(DateTime, nullable=True)
    email = Column(String)

class Broker(Base):
    __tablename__ = 'broker'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    opt_out_url = Column(String)
    process_type = Column(String)
    requires_captcha = Column(Boolean)
    avg_removal_days = Column(Integer)

class Listing(Base):
    __tablename__ = 'listing'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    broker_id = Column(Integer, ForeignKey('broker.id'))
    matched_url = Column(String)
    confidence_score = Column(Float)
    status = Column(String)
    found_at = Column(DateTime, default=datetime.utcnow)
    submitted_at = Column(DateTime, nullable=True)
    removed_at = Column(DateTime, nullable=True)
    last_checked_at = Column(DateTime, nullable=True)