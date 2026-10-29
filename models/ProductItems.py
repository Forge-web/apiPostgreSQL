import uuid
from decimal import Decimal

from Base import Base
from sqlalchemy import (
	ForeignKey,
	Numeric,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class ProductItems(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "ProductItems"

	product_id: Mapped[int] = mapped_column(
		ForeignKey("Products.id", ondelete="SET NULL"), nullable=False
	)
	invoice_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("Invoices.id", ondelete="RESTRICT"), nullable=False
	)
	quantity: Mapped[Decimal] = mapped_column(
		Numeric(precision=10, scale=3), nullable=False
	)
	price: Mapped[Decimal] = mapped_column(
		Numeric(precision=10, scale=2), nullable=False
	)
	quantity_sum: Mapped[Decimal] = mapped_column(
		Numeric(precision=12, scale=2), nullable=False
	)
