
from pydantic import BaseModel

class SetupCreate(BaseModel):
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float

class Setup(SetupCreate):
    id: int
    class Config:
        from_attributes = True

class JournalEntryBase(BaseModel):
    date: str
    trade_summary: str
    emotions: str
    discipline_rating: int

class JournalEntry(JournalEntryBase):
    id: int
    class Config:
        from_attributes = True
