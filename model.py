from db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(255), unique = True)
    password = Column(String(255))

class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    resume_text = Column(Text)
    result = Column(Text)