from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pony.orm import db_session

import app.settings as settings
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@db_session
def authenticate_user(username: str, password: str) -> User | None:
    """
    Checks if username / password are valid credentials in the database

    Returns:
        User or None: Relevant User matching credentials otherwise None
    """
    user = User.get(username=username)
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


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Retrieves user according to the username encoded in the JWT token

    Returns:
        User: User associated with the JWT token
    Raises:
        HTTPException: When JWT token is invalid, expired, or references a user
            not present in the database
    """
    invalid_credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        decoded_token = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
    except JWTError:
        raise invalid_credentials_exception

    username: str = decoded_token.get("sub")
    if username is None:
        raise invalid_credentials_exception

    with db_session:
        user = User.get(username=username)

    if user is None:
        raise invalid_credentials_exception

    return user
