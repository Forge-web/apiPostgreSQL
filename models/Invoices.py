import enum
from decimal import Decimal

from Base import Base
from sqlalchemy import (
	Enum,
	Numeric,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class InvoiceTypes(enum.Enum):
	Supply = "Поставка"
	Sale = "Продажа"
	Return = "Возврат"


class Invoices(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "Invoices"

	invoiceType: Mapped[InvoiceTypes] = mapped_column(
		Enum(InvoiceTypes), nullable=False
	)
	invoiceSum: Mapped[Decimal] = mapped_column(
		Numeric(precision=10, scale=2), nullable=False
	)
