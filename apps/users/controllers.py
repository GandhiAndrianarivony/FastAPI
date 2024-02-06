from passlib.context import CryptContext

from apps.users.models import User
from .helpers import hash_password


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
