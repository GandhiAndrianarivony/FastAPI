from fastapi import HTTPException, status

from apps.users.models import User
from api.helpers import Hash
from . import helpers

hash = Hash()


def login(request, db):
    user = db.query(User).filter(User.email == request.username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user = user.first()
    if not hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Wrong password"
        )
    
    access_token = helpers.create_access_token(
        data={"sub": user.email},
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
