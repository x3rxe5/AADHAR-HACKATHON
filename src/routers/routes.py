from fastapi import APIRouter

route = APIRouter()

@route.get("/")
async def test_route():
    return {
        "test":"it works"
    }