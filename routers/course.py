from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.course import Course
from core.dependencies import get_db

course_router = APIRouter(
    prefix="/course",
    tags=["course"]
)


@course_router.get("/")
async def get_all_courses(db: Session = Depends(get_db)):
    data = db.query(Course).all()
    return {"courses": data}

