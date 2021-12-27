
from fastapi import FastAPI
from .database import Base, engine
from .router import course, user, authentication

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(course.router)
app.include_router(user.router)
app.include_router(authentication.router)

