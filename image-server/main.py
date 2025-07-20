from fastapi import FastAPI, UploadFile, File
from utils.similarity import dummy_similarity_check

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = dummy_similarity_check(contents)
    return {"result": result}
