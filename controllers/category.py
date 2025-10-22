from typing import List

from fastapi import APIRouter

from schemas.category import Category

router =APIRouter(prefix='/category', tags=['Category'] )

@router.get('/', response_model=List[Category])
async def get_category():
    return []
