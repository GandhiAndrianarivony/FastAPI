from typing import List

from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api import db_connection

from apps.blogs import schema as blog_schema
from apps.users import schema as user_schema

from apps.blogs import controllers as blog_controllers
from apps.users import controllers as user_controllers


db_connection.Base.metadata.create_all(bind=db_connection.engine)

app = FastAPI()


@app.get("/blog", response_model=List[blog_schema.ShowBlog])
def list(db: Session = Depends(db_connection.get_db)):
    return blog_controllers.get_blogs(db)


@app.get(
    "/blog/{id}/", 
    status_code=status.HTTP_200_OK, 
    response_model=blog_schema.ShowBlog
)
def detail(id: int, db: Session = Depends(db_connection.get_db)):
    blog = blog_controllers.get_blog(id, db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: blog_schema.Blog, db: Session = Depends(db_connection.get_db)):
    return blog_controllers.create_blog(request, db)


@app.delete("/blog/{id}/", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(db_connection.get_db)):
    blog_controllers.delete_blog(id, db)
    return {"message": "DELETED", "status_code": status.HTTP_200_OK}


@app.put("/blog/{id}/", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: blog_schema.Blog, db: Session = Depends(db_connection.get_db)):
    return blog_controllers.update_blog(id, request, db)


@app.post('/user')
def create_user(request: user_schema.User,db: Session = Depends(db_connection.get_db)):
    return user_controllers.create_user(request, db)