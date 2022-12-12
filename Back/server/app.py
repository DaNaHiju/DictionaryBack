from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from server.models.mila import MilaSchema
from server.routes.mila import router as MilaRouter
from server.database import (
    fetch_one_mila, fetch_all_milim, add_mila, update_mila, delete_mila)

app = FastAPI()

app.include_router(MilaRouter, tags=["Mila"], prefix="/mila")

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def read_root():
    return {"Spanish": "Hebrew"}



# @app.get("/api/mila")
# async def get_mila():
#     response = await fetch_all_milim()
#     return response


# @app.get("/api/mila{spanish}", response_model=MilaSchema)
# async def get_one_mila(spanish):
#     response = await fetch_one_mila(spanish)
#     if response:
#         return response
#     raise HTTPException(404, f"the word {spanish} wasn't found")


# @app.post("/api/mila", response_model=MilaSchema)
# async def post_mila(mila: MilaSchema):
#     response = await add_mila(mila.dict())
#     if response:
#         return response
#     raise HTTPException(400, "something went wrong")


# @app.put("/api/mila{spanish}", response_model=MilaSchema)
# async def put_mila(spanish: str, hebrew: str, fonetica: str):
#     response = await update_mila(spanish, hebrew, fonetica)
#     if response:
#         return response
#     raise HTTPException(400, "something went wrong")


# @app.delete("/api/milon{spanish}")
# async def remove_mila(spanish):
#     response = await delete_mila(spanish)
#     if response:
#         return "Succesfully deleted"
#     raise HTTPException(404, f"the word {spanish} wasn't found")
