from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db_connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")