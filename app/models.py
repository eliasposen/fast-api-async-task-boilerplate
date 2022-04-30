from passlib.context import CryptContext
from pony.orm import Database, Required

import app.settings as settings

db = Database()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(db.Entity):
    username = Required(str, unique=True)
    hashed_password = Required(str)

    @staticmethod
    def hash_password(plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.hashed_password)


db.bind(
    provider=settings.DB_PROVIDER,
    host=settings.DB_HOST,
    database=settings.DB_NAME,
    port=settings.DB_PORT,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
)
db.generate_mapping(create_tables=True)
