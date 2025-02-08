from pydantic import BaseModel
from passlib.hash import bcrypt

class User(BaseModel):
    email: str
    phone: str
    preferred_language: str
    fcm_token: str
    password: str

    def set_password(self, password: str):
        self.password = bcrypt.hash(password)

    def check_password(self, password: str):
        return bcrypt.verify(password, self.password)