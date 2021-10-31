from typing import Optional
from fastapi import APIRouter
from src.schemas.schema import CreateAddress
from src.logic.parsing import parse_address
from starlette.requests import Request


route = APIRouter()

@route.post("/")
async def check_address(request:Request,res:CreateAddress,lang:Optional[str]=None):
    lang = request.query_params["lang"]    
    res_dict = parse_address(res,lang)
    return res_dict
    
