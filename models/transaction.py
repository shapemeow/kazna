from typing import Optional
from datetime import datetime
from sqlalchemy import ForeignKey, SmallInteger, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class Transaction(BaseModel):
    __tablename__ = 'transactions'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[int] = mapped_column(SmallInteger)  # 0-план, 1-завершен, 2-отменен
    value: Mapped[int] = mapped_column(Integer)
    from_account: Mapped[Optional[int]] = mapped_column(ForeignKey('accounts.id'), nullable=True)
    to_account: Mapped[Optional[int]] = mapped_column(ForeignKey('accounts.id'), nullable=True)
    from_agent: Mapped[Optional[int]] = mapped_column(ForeignKey('contacts.id'), nullable=True)
    to_agent: Mapped[Optional[int]] = mapped_column(ForeignKey('contacts.id'), nullable=True)
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey('categories.id'), nullable=True)
    attachment_id: Mapped[Optional[int]] = mapped_column(ForeignKey('attachments.id'), nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime)
