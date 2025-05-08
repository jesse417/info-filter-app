from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import torch

app = FastAPI()
device = 0 if torch.cuda.is_available() else -1
print(f"Device set to use {'cuda' if device == 0 else 'cpu'}")

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)

class SummaryRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(request: SummaryRequest):
    summary = summarizer(request.text, max_length=100, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}
