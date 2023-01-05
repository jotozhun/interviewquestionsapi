from models.theoricquestions import Testing


async def get_one() -> Testing:
    testing_question = await Testing.find_one()
    return testing_question

async def add_one(new_testing: Testing) -> Testing:
    testing_question = await Testing.create(new_testing)
    return testing_question

async def add_many(new_testings: list[Testing]) -> list[Testing]:
    testing_questions = await Testing.insert_many(new_testings)
    return testing_questions
