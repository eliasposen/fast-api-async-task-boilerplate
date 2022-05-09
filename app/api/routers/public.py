from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["public"])


@router.get("/jams")
async def read_jams():
    """Sample public facing endpoint that jams"""
    return {"jams": "♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪"}
