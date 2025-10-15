# Smart Task Planner

## Overview
Backend API for breaking down user goals into actionable tasks/timelines using GPT-4.

## Setup
1. Clone repo
2. Install requirements: `pip install -r requirements.txt`
3. Add your API key in `.env` as `OPENAI_API_KEY=sk-...`
4. Run server: `uvicorn main:app --reload`

## Usage
POST `/plan` with JSON:
