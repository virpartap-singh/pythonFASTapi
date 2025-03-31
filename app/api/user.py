from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.user import create_user, get_users
from app.schemas.user_schemas import UserCreate, UserResponse
from app.database import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    print("user data =", user , type(user))
    return await create_user(db, user)

@router.get("/", response_model=List[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)
