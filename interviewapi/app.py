import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import Document, Indexed, init_beanie

from fastapi import FastAPI

app = FastAPI()


class Product(Document):
    name: str                          # You can use normal types just like in pydantic
    description: Optional[str] = None
    # price: Indexed(float)              # You can also specify that a field should correspond to an index
    # category: Category                 # You can include pydantic models as well

class BasicQuestion(Document):
    question = str
    answer = str
    keywords = list[str]
    difficulty = str
    level = str

# This is an asynchronous example, so we will access it from an async function
async def example():
    # Beanie uses Motor async client under the hood
    client = AsyncIOMotorClient("mongodb+srv://dev-mongo-user:dev-mongo-password@recruitingcluster.pazjha0.mongodb.net/?retryWrites=true&w=majority")

    # Initialize beanie with the Product document class
    await init_beanie(database=client.interviewquestions, document_models=[BasicQuestion])

    # chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
    # Beanie documents work just like pydantic models
    # tonybar = Product(name="Tony's")#, price=5.95, category=chocolate)
    # # And can be inserted into the database
    # await tonybar.insert()
    question = BasicQuestion(question="Hello")
    await question.insert()


@app.get('/')
async def test_view():
    await example()
    return {"status:", 200}