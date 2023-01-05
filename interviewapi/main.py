from fastapi import FastAPI
from routes.generalprogramming import router as GeneralQuestionsRouter
from routes.databaseroutes import router as DatabaseQuestionsRouter
from routes.testingroutes import router as TestingQuestionsRouter
from config.config import initiate_database

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()

app.include_router(GeneralQuestionsRouter, tags=["general-programming"], prefix="/generalquestion")
app.include_router(DatabaseQuestionsRouter, tags=["database"], prefix="/databasequestion")
app.include_router(TestingQuestionsRouter, tags=["testing"], prefix="/testingquestion")
