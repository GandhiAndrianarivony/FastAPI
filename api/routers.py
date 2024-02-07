from fastapi import FastAPI
from api import db_connection
from apps.authentications.routers import authentication


from apps.blogs.routers import blog
from apps.users.routers import user


db_connection.Base.metadata.create_all(bind=db_connection.engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
