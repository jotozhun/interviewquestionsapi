from models.theoricquestions import Databases


async def get_one() -> Databases:
    database_question = await Databases.find_one()
    return database_question

async def add_one(new_database: Databases) -> Databases:
    database_question = await Databases.create(new_database)
    return database_question
