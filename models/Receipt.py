import uuid

from Base import Base
from sqlalchemy import (
	ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class Receipt(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "Checks"

	organizationId: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("Organizations.id", ondelete="RESTRICT"), nullable=False
	)
