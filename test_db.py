import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, AsyncSessionLocal  # Ensure correct import
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = "postgresql+asyncpg://postgres:Liberty%4023@127.0.0.1:5432/rp2025"

async def test_connection():
    try:
        engine = create_async_engine(DATABASE_URL, echo=True)
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed:", e)

asyncio.run(test_connection())
