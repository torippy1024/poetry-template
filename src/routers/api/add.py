from fastapi import APIRouter
from src.schemas.api.add import ApiAddGetResponse

addRouter = APIRouter()


@addRouter.get("", response_model=ApiAddGetResponse)
async def main(a: float, b: float):
    return ApiAddGetResponse(answer=(a + b))
