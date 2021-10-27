from fastapi import APIRouter
from src.schemas.schema import CreateAddress
from src.logic.parsing import parse_address

route = APIRouter()

@route.get("/",response_model=CreateAddress)
async def check_address(res:CreateAddress):
    res_dict = parse_address(res)
    return res_dict
