from fastapi import FastAPI, Request
from pydantic import BaseModel
from api import process_email

app = FastAPI()

class EmailRequest(BaseModel):
    email: str

@app.post("/")
async def classify_email(req: EmailRequest):
    result = process_email(req.email)
    return result
@app.get("/")
def read_root():
    return {"message": "Email Classifier API is running. Go to /docs to test."}