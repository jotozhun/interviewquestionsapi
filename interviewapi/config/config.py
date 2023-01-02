from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.theoricquestions import *

async def initiate_database():
    client = AsyncIOMotorClient("<mongo-server>")
    await init_beanie(database=client.interviewquestions,
                      document_models=[GeneralProgramming])
