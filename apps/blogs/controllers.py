from apps.blogs.models import Blog


def create_blog(request: Blog, db):
    new_blog = Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blogs(db):
    blogs = db.query(Blog).all()
    return blogs


def get_blog(id: int, db):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog