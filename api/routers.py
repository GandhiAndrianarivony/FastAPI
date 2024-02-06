from typing import Optional

from fastapi import FastAPI, Depends, status, Response
from sqlalchemy.orm import Session

from apps.blogs.schema import Blog
from apps.blogs import controllers as blog_controllers, db_connection


db_connection.Base.metadata.create_all(bind=db_connection.engine)

app = FastAPI()


@app.get("/blog")
def list(db: Session = Depends(db_connection.get_db)):
    return blog_controllers.get_blogs(db)


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All unpublished blogs"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def detail(id: int, response: Response, db: Session = Depends(db_connection.get_db)):
    blog = blog_controllers.get_blog(id, db)
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
    return blog


@app.get("/blog/{id}/comments/")
def comments(id):
    return {"data": ["1", "2"]}


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(db_connection.get_db)):
    return blog_controllers.create_blog(request, db)
