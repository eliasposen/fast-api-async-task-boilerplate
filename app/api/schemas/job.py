import queue
from datetime import datetime
from typing import Any
from unittest import result

from pydantic import BaseModel
from rq.job import Job as RQJob


class Job(BaseModel):
    job_id: str
    name: str
    queue: str
    status: str
    result: Any
    created_at: datetime

    @classmethod
    def from_rq(cls, rq_job: RQJob) -> "Job":
        """Serializes RQ Job into Job schema"""
        return cls(
            job_id=rq_job.id,
            name=rq_job.func_name.split(".")[-1],
            queue=rq_job.origin,
            status=rq_job.get_status(),
            result=rq_job.result,
            created_at=rq_job.created_at,
        )
