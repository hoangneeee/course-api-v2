from typing import List

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
async def create_user(request: schemas.User, db: Session = Depends(get_db),
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
async def show_user(username: str, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return user


'''Show All User'''
@router.get('/', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
async def show_all_user(db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    users = db.query(models.User).all()
    return users


'''Add coin'''
@router.put('/{username}', status_code=status.HTTP_202_ACCEPTED)
async def add_coin(username: str, request: schemas.AddCoin, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(oauth2.get_current_user)):
    coin = db.query(models.User).filter(models.User.username == username)
    if not coin.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    coin.update(dict(request))
    db.commit()
    return f"Added {request.coin} coins "

