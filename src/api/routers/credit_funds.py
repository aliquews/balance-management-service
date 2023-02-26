from fastapi import APIRouter


router = APIRouter(
    tags=["Сrediting funds to the user's account"],
    
)


router.post("/fund")
async def credit_fund():
    pass