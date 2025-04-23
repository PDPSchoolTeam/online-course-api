from fastapi import FastAPI
from routers.user import auth_router
from core.db import engine

from models.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
