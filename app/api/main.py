from fastapi import FastAPI

from app.api.routers import auth, jobs, public, users

app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(public.router)
app.include_router(jobs.router)
