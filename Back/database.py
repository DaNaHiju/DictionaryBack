from model import MilaSchema
# driver for mongodb
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.MilonList
collection = database.get_collection("milon_collection")

# helper


def mila_helper(mila) -> dict:
    return {
        "spanish": str(mila["spanish"]),
        "hebrew": str(mila["hebrew"]),
        "fonetica": str(mila["fonetica"]),
    }

# CRUD functions

# fetch one

# async def fetch_one_mila(spanish):
#     document = await collection.find_one({"spanish": spanish})
#     return document


async def fetch_one_mila(spanish: str) -> dict:
    mila = await collection.find_one({"spanish": spanish})
    return mila

# fetch all

# async def fetch_all_milim():
#     milim = []
#     cursor = collection.find({})
#     async for document in cursor:
#         milim.append(MilaSchema(**document))
#     return milim


async def fetch_all_milim():
    milim = []
    async for mila in collection.find():
        milim.append(mila_helper(mila))
        return milim


async def new_mila(mila):
    document = mila
    result = await collection.insert_one(document)
    return document


async def update_mila(spanish, hebrew, fonetica):
    docu = await collection.update_one({"spanish": spanish}, {"$set": {"hebrew": hebrew}}, {"$set": {"fonetica": fonetica}})
    document = await collection.find_one({"spanish": spanish})

    return document


async def delete_mila(spanish):
    await collection.delete_one({"spanish": spanish})
    return True
