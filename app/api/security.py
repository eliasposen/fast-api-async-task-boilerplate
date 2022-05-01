from datetime import datetime, timedelta

from fastapi import Depends
from jose import JWTError, jwt
from pony.orm import db_session

import app.settings as settings
from app.models import User


@db_session()
def get_user(username: str) -> User | None:
    """Retreives user from db if it exists"""
    return User.get(username=username)


@db_session
def authenticate_user(username: str, password: str) -> User | None:
    """
    Checks if username / password are valid credentials in the database

    Returns:
        User or None: Relevant User matching credentials otherwise None
    """
    user = get_user(username)
    if user is None or not user.verify_password(password):
        return None

    user.last_login = datetime.utcnow()

    return user


def create_jwt_access_token(user: User) -> str:
    """
    Creates JWT access token for given user

    Returns:
        str: Encoded JWT access token
    """
    to_encode = {
        "sub": user.username,
        "exp": datetime.utcnow()
        + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MIN),
    }
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
