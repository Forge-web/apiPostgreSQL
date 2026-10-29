from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
import uuid


class IdMixin:
	@declared_attr.directive
	def id(cls) -> Mapped[uuid.UUID]:
		return mapped_column(
			UUID(as_uuid=True),
			primary_key=True,
			server_default=("gen_random_uuid()"),
		)
