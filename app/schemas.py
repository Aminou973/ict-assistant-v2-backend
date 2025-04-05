from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# SETUPS
class SetupBase(BaseModel):
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float

class SetupCreate(SetupBase):
    probability_score: Optional[float] = None
    bias: Optional[str] = None
    confidence_comment: Optional[str] = None

class Setup(SetupCreate):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# JOURNAL
class JournalEntryCreate(BaseModel):
    emotions: str
    thoughts: str

class JournalEntry(JournalEntryCreate):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# ANALYZE
class AnalyzeRequest(BaseModel):
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float

class AnalyzeResponse(BaseModel):
    probability_score: float
    bias: str
    confidence_comment: str

# STATS
class Stats(BaseModel):
    total_trades: int
    win_rate: float
    average_rr: float
    best_setup: Optional[str]
    last_updated: Optional[datetime]

    class Config:
        from_attributes = True