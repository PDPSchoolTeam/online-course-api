from pydantic import BaseModel


class LessonOut(BaseModel):
    id: int
    course_id: int
    title: str
    video_url: str
    content: str


class LessonCreate(BaseModel):
    course_id: int
    title: str
    video_url: str
    content: str


class LessonUpdate(BaseModel):
    title: str
    video_url: str
    content: str
