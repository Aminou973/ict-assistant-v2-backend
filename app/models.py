from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base

class Setup(Base):
    __tablename__ = "setups"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    context = Column(Text)
    entry_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    risk_reward = Column(Float)
    probability_score = Column(Float)
    bias = Column(String)
    confidence_comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    emotions = Column(Text)
    thoughts = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    total_trades = Column(Integer)
    win_rate = Column(Float)
    average_rr = Column(Float)
    best_setup = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)