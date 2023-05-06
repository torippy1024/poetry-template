from fastapi import APIRouter
from src.routers.api.add import addRouter

router = APIRouter()
router.include_router(addRouter, prefix="/add")
