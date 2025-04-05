from fastapi import FastAPI
from app.routers import users, setups, journal, auth  #
from app.routers import discord_test

app = FastAPI()

app.include_router(users.router)
app.include_router(setups.router)
app.include_router(journal.router)
app.include_router(auth.router)
app.include_router(discord_test.router)


@app.get("/")
def root():
    return {"message": "ICT Assistant V2 Backend Ready"}






