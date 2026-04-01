from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class Currency(BaseModel):
    __tablename__ = 'currencies'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    symbol: Mapped[str] = mapped_column(String(5))
