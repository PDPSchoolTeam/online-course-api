from models.base import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, validates


class Rating(BaseModel):
    __tablename__ = "rating"

    starts: Mapped[int] = mapped_column(nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lesson.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    @validates('starts')
    def validate_starts(self, key, starts):
        if not 1 <= starts <= 5:
            raise ValueError("Rating 1 va 5 oralig'ida bo'lishi kerak")  # noqa
        return starts
