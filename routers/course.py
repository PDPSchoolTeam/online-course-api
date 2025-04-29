from fastapi import APIRouter, status, HTTPException
from models.course import Course
from models.user import User
from core.dependencies import DBSessionDep, CurrentUserDep
from schemas.course import CourseCreate, CourseOut, CourseUpdate

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
    author = db.query(User).filter(User.id == course.author_id).first()
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id {course.author_id} not found"
        )
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@course_router.put("/{course_id}", response_model=CourseOut, status_code=status.HTTP_200_OK)
async def update_course(course_id: int, course: CourseUpdate, db: DBSessionDep):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )

    for field, value in course.dict(exclude_unset=True).items():
        setattr(db_course, field, value)

    db.commit()
    db.refresh(db_course)
    return db_course


@course_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: DBSessionDep):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )

    db.delete(db_course)
    db.commit()
    return None
