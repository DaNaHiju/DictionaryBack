
# Driver for mongodb

import motor.motor_asyncio
from bson.objectid import ObjectId

#MONGO_DETAILS = 'mongodb://localhost:27017'
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.milon

collection = database.get_collection("milon_collection")

# helper


def mila_helper(mila) -> dict:
    return {
        "id": str(mila["_id"]),
        "spanish": (mila["spanish"]),
        "hebrew": (mila["hebrew"]),
        "fonetica": (mila["fonetica"]),
    }


# Fetch one mila

async def fetch_one_mila(id: str) -> dict:
    mila = await collection.find_one({"_id": ObjectId(id)})
    if mila:
        return mila_helper(mila)


# Fetch all

async def fetch_all_milim():
    milon = []
    async for mila in collection.find():
        milon.append(mila_helper(mila))
    return milon

# Add mila


async def add_mila(mila_data: dict) -> dict:
    mila = await collection.insert_one(mila_data)
    new_mila = await collection.find_one({"_id": mila.inserted_id})
    return mila_helper(new_mila)

# Update mila


# async def update_mila(id: str, data: dict):
#     # Return false in case an empty request is sent
#     if len(data) < 1:
#         return False
#     mila = await collection.find_one({"_id": ObjectId(id)})
#     if mila:
#         updated_mila = await collection.update_one(
#             {"_id", ObjectId(id)}, {"$set": data}
#         )
#         if updated_mila:
#             return True
#         return False
async def update_mila(id: str, data: dict):
    # Return false in case an empty request is sent
    if len(data) < 1:
        return False
    mila = await collection.find_one({"_id": ObjectId(id)})
    if mila:
        updated_mila = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_mila.modified_count:
            return True
        return False

# Delete


async def delete_mila(id: str):
    mila = await collection.find_one({"_id": ObjectId(id)})
    if mila:
        await collection.delete_one({"_id": ObjectId(id)})
        return True


# CRUD functions

# Fetch one

# async def fetch_one_mila(spanish):
#     document = await collection.find_one({"spanish": spanish})
#     return document
# Fetch all

# async def fetch_all_milim():
#     milim = []
#     cursor = collection.find({})
#     async for document in cursor:
#         milim.append(MilaSchema(**document))
#     return milim
# Create new mila

# async def new_mila(mila):
#     document = mila
#     result = await collection.insert_one(document)
#     return document

# Update mila

# async def update_mila(spanish, hebrew, fonetica):
#     docu = await collection.update_one({"spanish": spanish}, {"$set": {"hebrew": hebrew}}, {"$set": {"fonetica": fonetica}})
#     document = await collection.find_one({"spanish": spanish})

#     return document
# Delete mila

# async def delete_mila(spanish):
#     await collection.delete_one({"spanish": spanish})
#     return True
