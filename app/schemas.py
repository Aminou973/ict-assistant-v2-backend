from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

class SetupCreate(BaseModel):
    user_id: int
    date: datetime
    type: str
    context: str
    probability_score: Optional[int]
    result: Optional[str]
    rr: Optional[str]

class Setup(BaseModel):
    id: int
    user_id: int
    date: datetime
    type: str
    context: str
    probability_score: Optional[int]
    result: Optional[str]
    rr: Optional[str]

    class Config:
        orm_mode = True

class JournalEntryCreate(BaseModel):
    user_id: int
    date: datetime
    emotions: str
    plan_vs_reality: str
    discipline_score: int

class JournalEntry(BaseModel):
    id: int
    user_id: int
    date: datetime
    emotions: str
    plan_vs_reality: str
    discipline_score: int

    class Config:
        orm_mode = True
