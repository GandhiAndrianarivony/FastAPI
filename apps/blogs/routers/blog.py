from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

from apps.blogs import repositories as blog_repositories
from apps.blogs import schema as blog_schema
from apps.users import schema as user_schema
from api import db_connection

from apps.authentications import oauth2


router = APIRouter(tags=["Blogs"], prefix="/blog")


@router.get("/", response_model=List[blog_schema.ShowBlog])
def list(
    db: Session = Depends(db_connection.get_db),
    current_user: user_schema.User = Depends(oauth2.get_current_user),
):
    return blog_repositories.get_blogs(db)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=blog_schema.ShowBlog
)
def detail(id: int, db: Session = Depends(db_connection.get_db)):
    blog = blog_repositories.get_blog(id, db)
    return blog


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: blog_schema.Blog, db: Session = Depends(db_connection.get_db)):
    return blog_repositories.create_blog(request, db)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(db_connection.get_db)):
    blog_repositories.delete_blog(id, db)
    return {"message": "DELETED", "status_code": status.HTTP_200_OK}


@router.put("/{id}/", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: blog_schema.Blog, db: Session = Depends(db_connection.get_db)):
    blog = blog_repositories.update_blog(id, request, db)
    return blog
