from sqlalchemy import Column, String, Integer, Float, UniqueConstraint, BigInteger

from .database import Base


class User(Base):
    __tablename__="custom_users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    balance = Column(Float, default = 0)

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}('
            f'id={self.id}, username={self.username})>'
        )