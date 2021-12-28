from http.client import HTTPException
from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from course import models, schemas, oauth2
from course.database import get_db

router = APIRouter(
    prefix="/course",
    tags=['Courses'],
)


'''Show all Course'''
@router.get("/", response_model=List[schemas.ShowCourse])
async def get_all_course(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses


'''Show course with Id'''
@router.get("/{id}", response_model=schemas.ShowCourse, status_code=status.HTTP_200_OK)
async def get_course_with_id(id: int, db: Session = Depends(get_db),
                             current_user: schemas.User = Depends(oauth2.get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with the id {id} is not available")
    return course


'''Create Course'''
@router.post('/', response_model=schemas.ShowCourse, status_code=status.HTTP_201_CREATED)
async def create_course(request: schemas.Course, db: Session = Depends(get_db),
                        current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_course =models.Course(
        course_name = request.course_name,
        price = request.price,
        author_id = request.author_id,
        lesson = request.lesson,
        status = request.status,
        category = request.category,
        description = request.description,
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


'''Update Course with Id'''
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async  def update_course(id, request: schemas.Course,  db: Session = Depends(get_db),
                         current_user: schemas.User = Depends(oauth2.get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == id)
    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    course.update(dict(request))
    db.commit()
    return 'Update OK'


'''Delete Course with ID'''
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_course(id: int, db: Session = Depends(get_db),
                         current_user: schemas.User = Depends(oauth2.get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == id)
    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    course.delete(synchronize_session=False)
    db.commit()
    return 'Done'