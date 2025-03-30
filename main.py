from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from database import get_db
from schemas import UserCreate

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

# @app.post("/users/")
# async def create_user(user: dict):
#     print("inside user")
#     return {"message": "User endpoint hit!", "user": user}

@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    print("inside user")
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


