import os

from beanie import init_beanie
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from models.theoricquestions import theoric_programming_models

async def initiate_database():
    load_dotenv()
    client = AsyncIOMotorClient(os.environ.get('MONGO_SERVER_URL'))
    await init_beanie(database=client.interviewquestions,
                      document_models=theoric_programming_models)
