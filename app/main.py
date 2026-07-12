from fastapi import FastAPI, UploadFile, File
from app.models import AnalyzeRequest

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    return {"word_count": len(request.text.split())}


@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }
