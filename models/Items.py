import uuid

from Base import Base
from sqlalchemy import (
	ForeignKey,
	Numeric,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class Items(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "Items"

	product_items_id: Mapped[int] = mapped_column(
		ForeignKey(
			"ProductItems.id",
		)
	)
	receipt_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("Receipt.id", ondelete="RESTRICT"), nullable=False
	)
	quantity: Mapped[float] = mapped_column(
		Numeric(precision=10, scale=3), nullable=False
	)
	item_sum: Mapped[float] = mapped_column(
		Numeric(precision=10, scale=2), nullable=False
	)
