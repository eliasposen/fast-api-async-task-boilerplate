from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

import app.api.schemas as schemas
import app.api.security as security
from app.models import User

app = FastAPI()


@app.post("/token")
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


@app.get("/public")
async def read_public():
    return {"public": True, "jams": "♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(security.get_current_user)):
    return schemas.User.from_orm(current_user)
