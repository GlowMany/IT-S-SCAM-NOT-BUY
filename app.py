from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import re
import json
import os

app = FastAPI()

class DutchHCaptchaAI:
    def __init__(self, log_file="hcaptcha_log.json"):
        self.tokenizer = AutoTokenizer.from_pretrained("DTAI-KULeuven/robbert-2022-dutch-base")
        self.model = AutoModelForSequenceClassification.from_pretrained("DTAI-KULeuven/robbert-2022-dutch-base")
        self.classifier = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer)
        self.log_file = log_file
        self.log = self._load_log()

    def _load_log(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_log(self):
        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(self.log, f, ensure_ascii=False, indent=2)

    def answer(self, question):
        # Clean question text
        cleaned_question = re.sub(r"aria/Antwoord a\.u\.b\.|'ja'|'nee'|\?", "", question.lower()).strip()

        # Return cached answer if exists
        if cleaned_question in self.log:
            return self.log[cleaned_question]

        # Get prediction from model pipeline
        result = self.classifier(cleaned_question)
        answer = "Ja" if result[0]["label"] == "POSITIVE" else "Nee"

        # Log answer for future
        self.log[cleaned_question] = answer
        self._save_log()
        return answer

# Instantiate AI
ai = DutchHCaptchaAI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/solve")
async def solve_hcaptcha(request: QuestionRequest):
    answer = ai.answer(request.question)
    return {"question": request.question, "answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
