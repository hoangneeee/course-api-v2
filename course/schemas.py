from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import Query, Body
from pydantic import BaseModel


'''Create Schemas Here'''
class Course(BaseModel):
    course_name: Optional[str]
    price: Optional[int]
    author_id: Optional[int]
    lesson: Optional[int]
    status: Optional[bool] = Query(default=True)
    category: Optional[str]
    description: Optional[str]
    update_at: Optional[datetime]

    class Config():
        orm_mode=True


class ShowCourse(BaseModel):
    id: int
    course_name: Optional[str]
    price: Optional[int]
    author_id: Optional[int]
    lesson: Optional[int]
    status: Optional[bool]
    category: Optional[str]
    description: Optional[str]

    class Config():
        orm_mode = True


class User(BaseModel):
    username: Optional[str] = Body(min_length=1, max_length=255, default=None)
    password: Optional[str]
    gmail: Optional[str]
    phone: Optional[str] = Body(default=0)
    age: Optional[int]
    gender: Optional[str] = Body(default='male')


class ShowUser(BaseModel):
    id: int
    username: str
    gmail: str
    phone: str
    coin: int
    age: int
    gender: str
    course: List[ShowCourse]

    class Config():
        orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None