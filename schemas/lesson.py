from pydantic import BaseModel


class Lesson(BaseModel):
    id: int
    course_id: int
    title: str
    video_url: str
    content: str
