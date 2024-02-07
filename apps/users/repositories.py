from fastapi import HTTPException, status

from apps.users.models import User
from api.helpers import hash_password


def create_user(request, db):
    new_user = User(
        name=request.name, 
        email=request.email, 
        password=hash_password(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(id, db):
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user.first()
