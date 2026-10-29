import bcrypt
from Base import Base
from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.timeStampedMixin import TimeStampedMixin
from models.mixins.uuidMixin import IdMixin


class User(IdMixin, TimeStampedMixin, Base):
	__tablename__ = "users"

	username: Mapped[str] = mapped_column(
		String(50), unique=True, nullable=False
	)

	email: Mapped[str] = mapped_column(
		String(120), unique=True, nullable=False
	)

	_password_hash: Mapped[str] = mapped_column()

	# created_at: Mapped[datetime] = mapped_column(
	# 	server_default=text("TIMEZONE('utc', NOW())")
	# )

	@hybrid_property
	def password(self) -> str:
		return self._password_hash

	@password.setter
	def password_setter(self, plain_password: str) -> None:
		"""Auto hash password"""
		password_bytes = plain_password.encode("utf-8")
		salt = bcrypt.gensalt()
		hashed_bytes = bcrypt.hashpw(password_bytes, salt)

		self._password_hash = hashed_bytes.decode("utf-8")

	def check_password(self, plain_password: str) -> bool:
		password_bytes = plain_password.encode("utf-8")
		hash_bytes = self._password_hash.encode("utf-8")
		return bcrypt.checkpw(password_bytes, hash_bytes)
