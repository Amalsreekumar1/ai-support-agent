from fastapi import FastAPI

app = FastAPI(
    title="AI support agent",
    description="Backend API for an AI-powered customer support agent",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "AI Support Agent API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
