from fastapi import APIRouter, HTTPException, status
from rq.exceptions import NoSuchJobError
from rq.job import Job

import app.api.schemas as schemas
from app.jobs.queue import connection

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/{job_id}")
def read_job(job_id: str):
    """Retrive Job data associated with provided ID"""
    try:
        job = Job.fetch(job_id, connection=connection)
    except NoSuchJobError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No job with provided ID"
        )

    return schemas.Job.from_rq(job)
