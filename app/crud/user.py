from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user_models import User
from app.schemas.user_schemas import UserCreate

async def create_user( db: AsyncSession,user: UserCreate):
    print(user,"user inside")
    new_user = User(name=user.name, email=user.email)
    print(new_user,"new user")
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
