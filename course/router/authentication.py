
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas, database, models
from ..hashing import Hash
from .. import JWTtoken

router = APIRouter(
    prefix="/login",
    tags=["Authentication"],
)


'''Handle Login'''
@router.post('/')
def login(request: OAuth2PasswordRequestForm=Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Please double check your username or password")

    if not Hash.verify(hashed_password=user.password, plain_password=request.password):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Please double check your username or password")

    access_token = JWTtoken.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
