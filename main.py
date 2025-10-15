import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# For CORS (if building a frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class GoalRequest(BaseModel):
    goal: str

@app.post("/plan")
async def generate_plan(request: GoalRequest):
    prompt = (
        f"Break down this goal into actionable tasks with suggested deadlines and dependencies: {request.goal}. "
        "Output in bullet points, include timelines and dependencies."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a project manager expert in breaking down goals into action items."},
                {"role": "user", "content": prompt}
            ]
        )
        plan_text = response.choices[0].message.content
        return {"plan": plan_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
