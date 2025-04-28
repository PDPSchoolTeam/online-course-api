from fastapi import APIRouter, status
from models.course import Course
from core.dependencies import DBSessionDep, CurrentUserDep
from schemas.course import CourseCreate, CourseOut

course_router = APIRouter(
    prefix="/course",
    tags=["course"]
)


@course_router.get("/")
async def get_all_courses(db: DBSessionDep):
    data = db.query(Course).all()
    return {"courses": data}


@course_router.post("/", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(db: DBSessionDep, course: CourseCreate):
    new_course = Course(
        title=course.title,
        description=course.description,
        author_id=course.author_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course
