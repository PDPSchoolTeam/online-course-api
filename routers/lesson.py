from fastapi import APIRouter, status, HTTPException
from models.course import Lesson, Course
from core.dependencies import DBSessionDep, CurrentUserDep
from schemas.lesson import LessonOut, LessonCreate, LessonUpdate

lesson_router = APIRouter(
    prefix="/lesson",
    tags=["lesson"]
)


@lesson_router.get("/", response_model=list[LessonOut])
async def get_lesson(db: DBSessionDep, user: CurrentUserDep):
    data = db.query(Lesson).all()
    return data


@lesson_router.post("/", response_model=LessonOut, status_code=status.HTTP_201_CREATED)
async def create_lesson(db: DBSessionDep, lesson: LessonCreate, user: CurrentUserDep):
    db_course = db.query(Course).filter(Course.id == lesson.course_id).first()
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sizda bunday id {lesson.course_id} kurs mavjud emas!"  # noqa
        )
    new_lesson = Lesson(
        course_id=lesson.course_id,
        title=lesson.title,
        video_url=lesson.video_url,
        content=lesson.content
    )
    db.add(new_lesson)
    db.commit()
    return new_lesson


@lesson_router.put("/{lesson_id}", response_model=LessonOut, status_code=status.HTTP_200_OK)
async def lesson_update(lesson_id: int, db: DBSessionDep, user: CurrentUserDep, lesson: LessonUpdate):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not db_lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sizda bunday id {lesson_id} dars mavjud emas!"  # noqa
        )

    for field, value in lesson.dict(exclude_unset=True).items():
        setattr(db_lesson, field, value)

    db.commit()
    db.refresh(db_lesson)
    return db_lesson


@lesson_router.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(lesson_id: int, db: DBSessionDep, user: CurrentUserDep):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not db_lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sizda bunday id {lesson_id} dars mavjud emas!"  # noqa
        )

    db.delete(db_lesson)
    db.commit()
    return None
