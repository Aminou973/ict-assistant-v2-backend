from fastapi import FastAPI
from app.routers import users, setups, journal

app = FastAPI()

app.include_router(users.router)
app.include_router(setups.router)
app.include_router(journal.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "ICT Assistant V2 Backend Ready"}

from fastapi import FastAPI
from app.routers import users, setups, journal, auth  # ← bien ajouter "auth"

app = FastAPI()


