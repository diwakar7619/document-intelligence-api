from fastapi import FastAPI
from app.models import AnalyzeRequest

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    return {"word_count": len(request.text.split())}
