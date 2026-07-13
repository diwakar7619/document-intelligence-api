from fastapi import FastAPI, UploadFile, File
from app.models import AnalyzeRequest

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    return {"word_count": len(request.text.split())}


@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    content = await file.read()
    preview = content[:100]

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_in_bytes": len(content),
        "preview": str(preview),
    }
