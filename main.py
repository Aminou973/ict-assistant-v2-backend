
from fastapi import FastAPI
from app.routers import setups, journal, analyzer
from app.database import engine
from app import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(setups.router, prefix="/setups", tags=["Setups"])
app.include_router(journal.router, prefix="/journal", tags=["Journal"])
app.include_router(analyzer.router, tags=["Assistant IA"])
