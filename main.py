from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import setups, journal, analyzer, stats

app = FastAPI(title="ICT Assistant Backend")

app.include_router(setups.router, prefix="/setups", tags=["Setups"])
app.include_router(journal.router, prefix="/journal", tags=["Journal"])
app.include_router(analyzer.router, prefix="/analyze", tags=["Analyze"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])

@app.get("/")
def root():
    return {"message": "ICT Assistant V2 Backend Ready"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
