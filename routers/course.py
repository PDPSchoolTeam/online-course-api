from fastapi import APIRouter
from models.course import Course
from core.dependencies import DBSessionDep

course_router = APIRouter(
    prefix="/course",
    tags=["course"]
)


@course_router.get("/")
async def get_all_courses(db: DBSessionDep):
    data = db.query(Course).all()
    return {"courses": data}
