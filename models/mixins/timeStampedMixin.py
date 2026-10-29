from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import func


class TimeStampedMixin:
	@declared_attr.directive
	def created_at(cls) -> Mapped[datetime]:
		return mapped_column(server_default=func.now())

	@declared_attr.directive
	def updated_at(cls) -> Mapped[datetime]:
		return mapped_column(
			server_default=func.now(), onupdate=func.now()
		)
