from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DailyTemperature(Base):
    __tablename__ = 'daily_temperatures'

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)
    max_temp = Column(Float)
    min_temp = Column(Float)
    avg_temp = Column(Float)

engine = create_engine('sqlite:///temperatures.db')
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()
