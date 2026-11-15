from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.config import settings

# Automatically create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NOESIS AI Receptionist API",
    description="Backend REST API for NOESIS Intelligent Virtual Receptionist System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "app": "NOESIS AI Receptionist API",
        "status": "online",
        "version": "1.0.0"
    }
