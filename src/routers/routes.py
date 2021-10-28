from fastapi import APIRouter
from src.schemas.schema import CreateAddress
from src.logic.parsing import parse_address

route = APIRouter()

@route.post("/")
async def check_address(res:CreateAddress):
    res_dict = parse_address(res)
    return res_dict
