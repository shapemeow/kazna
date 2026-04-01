from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from models.basemodel import BaseModel


class Attachment(BaseModel):
    __tablename__ = 'attachments'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    link: Mapped[str] = mapped_column(Text)
