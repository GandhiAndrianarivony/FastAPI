from fastapi import HTTPException, status

from apps.blogs.models import Blog


def create_blog(request: Blog, db):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def get_blogs(db):
    blogs = db.query(Blog).all()
    return blogs


def get_blog(id: int, db):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status=status.HTTP_404_NOT_FOUND)
    return blog.first()


def delete_blog(id: int, db):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    blog.delete(synchronize_session=False)
    db.commit()


def update_blog(id: int, request, db):
    data = {**request.model_dump()}
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    blog.update(data)
    db.commit()
    return blog.first()
