from passlib.context import CryptContext


def hash_password(password):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.hash(password)
