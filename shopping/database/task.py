from datetime import datetime

from sqlalchemy import String, Integer, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Task(Base):
    __tablename__ = 'tasks'

    number_id: Mapped[int] = mapped_column('id_number', primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    due_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    assigned_user_id: Mapped[int] = mapped_column()

    def __init__(
            self,
            description: str,
            priority: int,
            due_date,
            assigned_user_id: int,
            is_completed: bool = False,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.assigned_user_id = assigned_user_id
        self.is_completed = is_completed

    def __repr__(self) -> str:
        return f'<Task (id={self.number_id})>'
