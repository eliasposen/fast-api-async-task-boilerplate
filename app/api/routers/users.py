from fastapi import APIRouter, Depends

import app.api.schemas as schemas
import app.api.security as security
import app.models as models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def read_users_me(current_user: models.User = Depends(security.get_current_user)):
    """Retrieve data about current authenticated user"""
    return schemas.User.from_orm(current_user)
