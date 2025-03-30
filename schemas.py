from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True  # Ensures SQLAlchemy model compatibility

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True  # Allows ORM model conversion
