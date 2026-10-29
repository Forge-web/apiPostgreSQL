from decimal import Decimal

from Base import Base
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin


class Products(TimeStampedMixin, Base):
	__tablename__ = "Products"
	id: Mapped[int] = mapped_column(
		BigInteger,
		primary_key=True,
		autoincrement=True,
	)
	name: Mapped[str] = mapped_column(String(255), nullable=False)
	type_product: Mapped[int] = mapped_column(
		ForeignKey("TypeProducts.id", ondelete="RESTRICT")
	)
	price: Mapped[Decimal] = mapped_column(
		Numeric(precision=10, scale=2), nullable=False
	)
