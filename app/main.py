from fastapi import FastAPI
from app.routers import tickets
from app.database import Base, engine

app = FastAPI(
    title="AI support agent",
    description="Backend API for an AI-powered customer support agent",
    version="0.1.0",
)

Base.metadata.create_all(bind = engine)
app.include_router(tickets.router)

@app.get("/")
def root():
    return {"message": "AI Support Agent API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
