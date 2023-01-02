from typing import List

from models.theoricquestions import *

basicquestion_collection = GeneralProgramming

async def get_generalprogramming(number_of_questions: int = 3) -> List[GeneralProgramming]:
    questions = await basicquestion_collection.all().to_list()
    return questions

async def add_generalprogramming(new_generalprogramming: GeneralProgramming) -> GeneralProgramming:
    question = await new_generalprogramming.create()
    return question
