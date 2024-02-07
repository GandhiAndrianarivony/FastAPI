from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api import db_connection

from apps.users import schema as user_schema
from apps.users import repositories as user_repositories


router = APIRouter(
    tags=["Users"],
    prefix="/user"
)


@router.post('/', response_model=user_schema.ShowUser)
def create_user(request: user_schema.User,db: Session = Depends(db_connection.get_db)):
    return user_repositories.create_user(request, db)


@router.get('/{id}', response_model=user_schema.ShowUser)
def detail(id: int, db: Session = Depends(db_connection.get_db)):
    return user_repositories.get_user(id, db)