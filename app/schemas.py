from pydantic import BaseModel

class SetupCreate(BaseModel):
    user_id: int
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float

class Setup(BaseModel):
    id: int
    user_id: int
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float

    class Config:
        from_attributes = True  # Pydantic v2
