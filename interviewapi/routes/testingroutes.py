from fastapi import APIRouter, Body
from http import HTTPStatus
from database.testingquestion import *
from models.theoricquestions import Testing, Response

router = APIRouter()

@router.get('/', response_model=Response)
async def retrieve_testingquestion():
    question = await get_one()
    return Response(status_code=HTTPStatus.ACCEPTED,
                    data=question)

@router.post("/", response_model=Response)
async def insert_testingquestion(new_testing: Testing = Body(...)) -> Response:
    _ = await add_one(new_testing)
    return Response(status_code=HTTPStatus.CREATED)

@router.post("/many", response_model=Response)
async def insert_many_testingquestion(new_testing: list[Testing] = Body(...)) -> Response:
    _ = await add_many(new_testing)
    return Response(status_code=HTTPStatus.CREATED)
