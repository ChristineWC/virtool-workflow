from pathlib import Path
from shutil import rmtree

from fixtures import fixture
from virtool_workflow.data_model import Job
from virtool_workflow.api.client import authenticated_http


@fixture
def results() -> dict:
    return {}


@fixture
def work_path(config: dict) -> Path:
    """A temporary working directory."""
    path = Path(config["work_path"])
    path.mkdir(parents=True, exist_ok=True)
    yield path
    rmtree(path)


@fixture
def proc(config: dict) -> int:
    """"The number of processes to use for multiprocess operations."""
    return config["proc"]


@fixture
def mem(config: dict) -> int:
    """The amount of RAM available to be used."""
    return config["mem"]


@fixture
def jobs_api_url(config: dict) -> str:
    """The URL of the jobs API."""
    return config["jobs_api_url"]


@fixture
async def _job(job_id, acquire_job, scope) -> Job:
    """The current job."""
    job = await acquire_job(job_id)

    scope["http"] = await authenticated_http(job.id, job.key, scope["http"])

    return job
