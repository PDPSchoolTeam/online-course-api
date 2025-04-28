from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    author_id: int  # FK to User


class CourseOut(BaseModel):
    id: int
    title: str
    description: str
    author_id: int

    class Config:
        orm_mode = True
