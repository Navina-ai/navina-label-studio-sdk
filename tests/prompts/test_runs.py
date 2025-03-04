# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import LabelStudio
from label_studio_sdk import AsyncLabelStudio
import typing
from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "organization": 1,
        "project": 1,
        "model_version": 1,
        "created_by": 1,
        "project_subset": "All",
        "status": "Pending",
        "job_id": "job_id",
        "created_at": "2024-01-15T09:30:00Z",
        "triggered_at": "2024-01-15T09:30:00Z",
        "predictions_updated_at": "2024-01-15T09:30:00Z",
        "completed_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "organization": "integer",
        "project": "integer",
        "model_version": "integer",
        "created_by": "integer",
        "project_subset": None,
        "status": None,
        "job_id": None,
        "created_at": "datetime",
        "triggered_at": "datetime",
        "predictions_updated_at": "datetime",
        "completed_at": "datetime",
    }
    response = client.prompts.runs.list(id=1, version_id=1, project=1, project_subset="All")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.runs.list(id=1, version_id=1, project=1, project_subset="All")
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "organization": 1,
        "project": 1,
        "model_version": 1,
        "created_by": 1,
        "project_subset": "All",
        "status": "Pending",
        "job_id": "job_id",
        "created_at": "2024-01-15T09:30:00Z",
        "triggered_at": "2024-01-15T09:30:00Z",
        "predictions_updated_at": "2024-01-15T09:30:00Z",
        "completed_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "organization": "integer",
        "project": "integer",
        "model_version": "integer",
        "created_by": "integer",
        "project_subset": None,
        "status": None,
        "job_id": None,
        "created_at": "datetime",
        "triggered_at": "datetime",
        "predictions_updated_at": "datetime",
        "completed_at": "datetime",
    }
    response = client.prompts.runs.create(id=1, version_id=1, project=1, project_subset="All")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.runs.create(id=1, version_id=1, project=1, project_subset="All")
    validate_response(async_response, expected_response, expected_types)
