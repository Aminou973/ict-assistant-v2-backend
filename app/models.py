
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Setup(Base):
    __tablename__ = "setups"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    context = Column(String)
    entry_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    risk_reward = Column(Float)

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    trade_summary = Column(String)
    emotions = Column(String)
    discipline_rating = Column(Integer)
