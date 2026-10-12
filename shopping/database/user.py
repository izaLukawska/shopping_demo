from datetime import datetime, date

from sqlalchemy import String, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __init__(self, username: str, password: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self) -> str:
        return f'<User id={self.user_id}, username={self.username}>'
