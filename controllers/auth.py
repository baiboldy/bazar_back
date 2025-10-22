from typing import Annotated

from fastapi import APIRouter, Cookie, Form

from schemas.user import UserPayload, BaseUser, UserResponse, LoginPayload
from schemas.auth import Cookies

router = APIRouter(prefix='/auth', tags=['auth'])


@router.get('/')
async def get_auth(cookies: Annotated[Cookies, Cookie()]):
    return cookies


@router.post('/login')
async def login(user: Annotated[LoginPayload, Form()]):
    return user
