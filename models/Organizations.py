from Base import Base
from sqlalchemy.orm import Mapped

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class Organizations(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "Organizations"

	name: Mapped[str]
	legalForm: Mapped[str]
