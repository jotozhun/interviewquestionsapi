from fastapi import APIRouter, Body
from http import HTTPStatus
from database.mongodatabase import *
from models.theoricquestions import Databases, Response

router = APIRouter()

@router.get('/', response_model=Response)
async def retrieve_one_databasequestion():
    question = await get_one_database()
    return Response(status_code=HTTPStatus.ACCEPTED,
                    data=question)

@router.post("/", response_model=Response)
async def insert_databasequestion(new_database: Databases = Body(...)) -> Response:
    question = await add_database(new_database)
    return Response(status_code=HTTPStatus.CREATED,
                    data=question)
