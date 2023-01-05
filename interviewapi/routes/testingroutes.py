from fastapi import APIRouter, Body
from http import HTTPStatus
from database.mongodatabase import *
from models.theoricquestions import Testing, Response

router = APIRouter()

@router.get('/', response_model=Response)
async def retrieve_testingquestion():
    question = await get_one_testing()
    return Response(status_code=HTTPStatus.ACCEPTED,
                    data=question)

@router.post("/", response_model=Response)
async def insert_testingquestion(new_testing: Testing = Body(...)) -> Response:
    question = await add_testing(new_testing)
    return Response(status_code=HTTPStatus.CREATED,
                    data=question)
