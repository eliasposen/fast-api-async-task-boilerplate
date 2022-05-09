from fastapi import FastAPI

from app.api.routers import auth, public, users

app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(public.router)
