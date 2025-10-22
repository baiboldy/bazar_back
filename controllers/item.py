from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Header

router = APIRouter(prefix='/item', tags=['Item'])


@router.get('/')
async def get_items(user_agent: Annotated[str | None, Header()] = None):
    return {
        "user_agent": user_agent
    }
