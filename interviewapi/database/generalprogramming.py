from models.theoricquestions import GeneralProgramming


async def get_one() -> GeneralProgramming:
    questions = await GeneralProgramming.find_one()
    return questions

async def add_one(new_generalprogramming: GeneralProgramming) -> GeneralProgramming:
    question = await new_generalprogramming.create()
    return question
