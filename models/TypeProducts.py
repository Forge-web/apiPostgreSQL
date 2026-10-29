from Base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin


class TypeProduct(TimeStampedMixin, Base):
	__tablename__ = "TypeProducts"
	id: Mapped[int] = mapped_column(
		Integer, primary_key=True, autoincrement=True
	)
	name: Mapped[str] = mapped_column(
		String(255), unique=True, nullable=False
	)
