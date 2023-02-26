from fastapi import APIRouter

from .routers.credit_funds import router as fund_router


router = APIRouter()


router.include_router(fund_router)