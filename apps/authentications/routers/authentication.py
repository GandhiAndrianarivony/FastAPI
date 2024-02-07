from fastapi import APIRouter, Depends
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from sqlalchemy.orm import Session

from apps.authentications.schema import Login
from api import db_connection

from apps.authentications import repositories

router = APIRouter(
    tags=['Auth']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_connection.get_db)):
    return repositories.login(request, db)