from model import Mila
# driver for mongodb
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Milon
collection = database.mila


async def fetch_one_mila(spanish):
    document = await collection.find_one({"spanish": spanish})
    return document


async def fetch_all_milim():
    milim = []
    cursor = collection.find({})
    async for document in cursor:
        milim.append(Mila(**document))
    return milim


async def new_mila(mila):
    document = mila
    result = await collection.insert_one(document)
    return document


async def update_mila(spanish, hebrew, fonetica):
    await collection.update_one({"spanish": spanish}, {"$set": {"hebrew": hebrew}}, {"$set": {"fonetica": fonetica}})
    document = await collection.find_one({"spanish": spanish})
    return document
