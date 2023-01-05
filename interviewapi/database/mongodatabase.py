from typing import List

from models.theoricquestions import *


async def get_one_generalprogramming(number_of_questions: int = 3) -> GeneralProgramming:
    questions = await GeneralProgramming.find_one()
    return questions

async def add_generalprogramming(new_generalprogramming: GeneralProgramming) -> GeneralProgramming:
    question = await new_generalprogramming.create()
    return question

async def get_one_testing() -> Testing:
    testing_question = await Testing.find_one()
    return testing_question

async def add_testing(new_testing: Testing) -> Testing:
    testing_question = await Testing.create(new_testing)
    return testing_question

async def get_one_database() -> Databases:
    database_question = await Databases.find_one()
    return database_question

async def add_database(new_database: Databases) -> Databases:
    database_question = await Databases.create(new_database)
    return database_question
