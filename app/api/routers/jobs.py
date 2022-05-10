import uuid

from fastapi import APIRouter, HTTPException, status
from rq.exceptions import NoSuchJobError
from rq.job import Job

import app.api.schemas as schemas
from app.jobs.queue import connection, queue
from app.jobs.sample_job import sleep_job

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/{job_id}", response_model=schemas.Job)
def read_job(job_id: uuid.UUID):
    """Retrive Job data associated with provided ID"""
    try:
        job = Job.fetch(str(job_id), connection=connection)
    except NoSuchJobError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No job with provided ID"
        )

    return schemas.Job.from_rq(job)


@router.post("/sleep", response_model=schemas.Job, status_code=status.HTTP_201_CREATED)
def start_sleep_job(sleep_job_in: schemas.SleepJobIn):
    """Start sample sleep job"""
    job = queue.enqueue(sleep_job, args=(sleep_job_in.sleep_sec,))
    return schemas.Job.from_rq(job)
