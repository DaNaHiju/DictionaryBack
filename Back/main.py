from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get("/")
def read_root():
    return {"ping":"pong"}

@app.get("/api/mila")
async def get_mila():
    return 1

@app.get("/api/mila{id}")
async def get_mila_id(id):
    return 1

@app.post("api/mila")
async def post_mila(mila):
    return 1 

@app.put("api/mila{id}")
async def update_mila(id, data):
    return 1 

@app.delete("api/milon{id}")
async def delete_mila(id):
    return 1 