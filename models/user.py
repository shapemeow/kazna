from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    login: Mapped[str] = mapped_column(String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
