from fastapi import APIRouter, Body
from http import HTTPStatus
from database.mongodatabase import *
from models.theoricquestions import GeneralProgramming, Response

router = APIRouter()

@router.get("/", response_model=Response)
async def retrieve_generalprogramming():
    questions = await get_one_generalprogramming()
    return {
        'status_code': 200,
        'response_type': 'OK',
        'description': 'All basic questions retrieved',
        'data': questions
    }

@router.post("/", response_model=Response)
async def insert_generalprogramming(new_general_programming: GeneralProgramming = Body(...)) -> Response:
    general_programming = await add_generalprogramming(new_general_programming)
    return Response(status_code=HTTPStatus.CREATED,
                    data=general_programming)
