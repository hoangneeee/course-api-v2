from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from course import schemas, models, hashing, oauth2
from course.database import get_db

router = APIRouter(
    prefix="/user",
    tags=['Users'],
)


'''Create User'''
@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_user = models.User(username=request.username, gmail=request.gmail,
                           password=hashing.Hash.bcrypt(request.password), phone=request.phone, age=request.age,
                           gender=request.gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


'''Show User'''
@router.get('/{username}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show_user(username: str, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return user

