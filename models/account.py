from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class Account(BaseModel):
    __tablename__ = 'accounts'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    currency_id: Mapped[int] = mapped_column(ForeignKey('currencies.id'))
    bank_id: Mapped[int] = mapped_column(ForeignKey('banks.id'))