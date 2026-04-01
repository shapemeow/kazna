from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class Bank(BaseModel):
    __tablename__ = 'banks'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
