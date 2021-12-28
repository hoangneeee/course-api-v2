from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, SmallInteger
from .database import Base
from sqlalchemy.orm import relationship


'''Create Model Here'''

'''Table Course'''
class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String)
    price = Column(Integer)
    lesson = Column(Integer)
    category = Column(String)
    description = Column(String)
    status = Column(Boolean)
    create_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime)
    author_id = Column(Integer, ForeignKey('user.id'))

    author = relationship("User", back_populates="course")



'''Table User'''
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    coin = Column(Integer, default=0)
    age = Column(SmallInteger)
    rule = Column(String)
    gender = Column(String)
    phone = Column(String)
    gmail = Column(String)

    course = relationship("Course", back_populates="author")

