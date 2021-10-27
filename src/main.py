# LOGIC Folder contains the algorithm behind this API

from fastapi import FastAPI
from .routers import routes

app = FastAPI()

@app.get("/")
async def ping():
    return "PONG"


app.include_router(  
    routes.route,
    prefix="/api/v1/address",
    tags=["address"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Unknown Error Occured"}},

)