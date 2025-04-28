from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    author_id: int  # FK to User
