from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    setups = relationship("Setup", back_populates="user")
    journal_entries = relationship("JournalEntry", back_populates="user")


class Setup(Base):
    __tablename__ = "setups"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String, nullable=False)  # 🔥 Cette ligne doit exister
    context = Column(String)
    entry_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    risk_reward = Column(Float)

    user = relationship("User", back_populates="setups")



class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    emotions = Column(Text)
    discipline_score = Column(Integer)
    notes = Column(Text)

    user = relationship("User", back_populates="journal_entries")
