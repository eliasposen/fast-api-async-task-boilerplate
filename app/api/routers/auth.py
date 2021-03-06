from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

import app.api.schemas as schemas
import app.api.security as security

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login
    """
    user = security.authenticate_user(login_data.username, login_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = security.create_jwt_access_token(user)

    return schemas.Token(access_token=access_token, token_type="Bearer")
