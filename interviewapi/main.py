from fastapi import FastAPI
from routes.generalprogramming import router as BasicQuestionsRouter
from config.config import initiate_database

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()

app.include_router(BasicQuestionsRouter, tags=["general-programming"], prefix="/generalquestion")
