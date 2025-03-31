from fastapi import FastAPI
from app.api.router import api_router
from app.database import engine
from app.models import user_models

app = FastAPI(title="FastAPI Multi-Model App")

# Register routers
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI App"}
