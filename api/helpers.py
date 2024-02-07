from passlib.context import CryptContext


def hash_password(password):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.hash(password)


class Hash:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password: str):
        return self.pwd_ctx.hash(password)

    def verify(
        self,
        request_password,
        hashed_user_password,
    ):
        return self.pwd_ctx.verify(request_password, hashed_user_password)
