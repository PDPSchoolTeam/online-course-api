from fastapi import APIRouter, status, HTTPException
from models.course import Lesson
from core.dependencies import DBSessionDep, CurrentUserDep
from schemas.lesson import Lesson

lesson_router = APIRouter(
    prefix="/lesson",
    tags=["lesson"]
)


@lesson_router.get("/")
async def get_lesson():
    ...
