from uuid import UUID

from flowdapt_sdk._compat import validate_model, model_dump
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.utils import build_version_header, build_request_data
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.dto import (
    V1Alpha1WorkflowResourceCreateRequest,
    V1Alpha1WorkflowResourceCreateResponse,
    V1Alpha1WorkflowResourceUpdateRequest,
    V1Alpha1WorkflowResourceUpdateResponse,
    V1Alpha1WorkflowResourceReadResponse,
    V1Alpha1WorkflowRunReadResponse,
)

WorkflowResourceType = "workflow"
WorkflowRunResourceType = "workflow_run"

WorkflowCreateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1WorkflowResourceCreateRequest,
        V1Alpha1WorkflowResourceCreateResponse,
    ),
}
WorkflowUpdateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1WorkflowResourceUpdateRequest,
        V1Alpha1WorkflowResourceUpdateResponse,
    ),
}
WorkflowReadRequestDTOs = {
    "v1alpha1": (None, V1Alpha1WorkflowResourceReadResponse),
}
WorkflowRunReadRequestDTOs = {
    "v1alpha1": (None, V1Alpha1WorkflowRunReadResponse),
}

WorkflowCreateRequest = V1Alpha1WorkflowResourceCreateRequest
WorkflowCreateResponse = V1Alpha1WorkflowResourceCreateResponse
WorkflowUpdateRequest = V1Alpha1WorkflowResourceUpdateRequest
WorkflowUpdateResponse = V1Alpha1WorkflowResourceUpdateResponse
WorkflowReadResponse = V1Alpha1WorkflowResourceReadResponse
WorkflowRunReadResponse = V1Alpha1WorkflowRunReadResponse

class WorkflowsAPI(BaseAPI):
    """
    WorkflowsAPI class provides methods for interacting with the Flowdapt Workflows API.

    It is not intended to be instantiated directly. Instead, it should be accessed
    via an instance of FlowdaptSDK.
    """
    async def list_workflows(self, version: str | None = None) -> list[WorkflowReadResponse]:
        """
        List all workflows.

        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: A list of workflows.
        :rtype: list[WorkflowReadResponse]
        """
        response_dto, _, version = build_request_data(WorkflowReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/workflows/",
            headers={APIVersionHeader: build_version_header(WorkflowResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return [validate_model(response_dto, data) for data in response.content]

    async def create_workflow(
        self,
        data: WorkflowCreateRequest | dict,
        version: str | None = None,
    ) -> WorkflowCreateResponse:
        """
        Create a new workflow.

        :param data: The data for the new workflow.
        :type data: WorkflowCreateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The new workflow.
        :rtype: WorkflowCreateResponse
        """
        response_dto, data, version = build_request_data(
            WorkflowCreateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.post(
            endpoint="/workflows/",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(WorkflowResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return validate_model(response_dto, response.content)

    async def get_workflow(
        self,
        identifier: str | UUID,
        version: str | None = None
    ) -> WorkflowReadResponse:
        """
        Get a workflow by its identifier.

        :param identifier: The identifier of the workflow.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The workflow.
        :rtype: WorkflowReadResponse
        """
        response_dto, _, version = build_request_data(WorkflowReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint=f"/workflows/{identifier}",
            headers={APIVersionHeader: build_version_header(WorkflowResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def update_workflow(
        self,
        identifier: str | UUID,
        data: WorkflowUpdateRequest | dict,
        version: str | None = None,
    ) -> WorkflowUpdateResponse:
        """
        Update a workflow.

        :param identifier: The identifier of the workflow.
        :type identifier: str | UUID
        :param data: The data for the updated workflow.
        :type data: WorkflowUpdateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The updated workflow.
        :rtype: WorkflowUpdateResponse
        """
        response_dto, data, version = build_request_data(
            WorkflowUpdateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.put(
            endpoint=f"/workflows/{identifier}",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(WorkflowResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def delete_workflow(
        self,
        identifier: str | UUID,
        version: str | None = None,
    ) -> None:
        """
        Delete a workflow by its identifier.

        :param identifier: The identifier of the workflow.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: None
        """
        response_dto, _, version = build_request_data(WorkflowReadRequestDTOs, version=version)

        response = await self.client.delete(
            endpoint=f"/workflows/{identifier}",
            headers={APIVersionHeader: build_version_header(WorkflowResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def list_workflow_runs(
        self,
        identifier: str | UUID,
        limit: int = 10,
        version: str | None = None,
    ) -> list[WorkflowRunReadResponse]:
        """
        List all runs for a workflow.

        :param identifier: The identifier of the workflow.
        :type identifier: str | UUID
        :param limit: The maximum number of runs to return.
        :type limit: int
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: A list of workflow runs.
        :rtype: list[WorkflowRunReadResponse]
        """
        response_dto, _, version = build_request_data(WorkflowRunReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint=f"/workflows/{identifier}/run",
            headers={APIVersionHeader: build_version_header(WorkflowRunResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier},
            query={"limit": limit}
        )

        return [validate_model(response_dto, data) for data in response.content]

    async def get_workflow_run(
        self,
        identifier: str | UUID,
        version: str | None = None,
    ) -> WorkflowRunReadResponse:
        """
        Get a workflow run by its identifier.

        :param identifier: The identifier of the workflow run.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The workflow run.
        :rtype: WorkflowRunReadResponse
        """
        response_dto, _, version = build_request_data(WorkflowRunReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint=f"/workflows/run/{identifier}",
            headers={APIVersionHeader: build_version_header(WorkflowRunResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def delete_workflow_run(
        self,
        identifier: str | UUID,
        version: str | None = None,
    ) -> WorkflowRunReadResponse:
        """
        Delete a workflow run by its identifier.

        :param identifier: The identifier of the workflow run.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The deleted workflow run.
        :rtype: WorkflowRunReadResponse
        """
        response_dto, _, version = build_request_data(WorkflowRunReadRequestDTOs, version=version)

        response = await self.client.delete(
            endpoint=f"/workflows/run/{identifier}",
            headers={APIVersionHeader: build_version_header(WorkflowRunResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def run_workflow(
        self,
        identifier: str | UUID,
        input: dict | None = None,
        wait: bool = True,
        namespace: str | None = None,
        version: str | None = None,
    ) -> WorkflowRunReadResponse:
        """
        Run a workflow.

        :param identifier: The identifier of the workflow to run.
        :type identifier: str | UUID
        :param input: The input data for the workflow.
        :type input: dict | None
        :param wait: Whether to wait for the run to complete.
        :type wait: bool
        :param namespace: The namespace to run the workflow in.
        :type namespace: str | None
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The workflow run.
        :rtype: WorkflowRunReadResponse
        """
        response_dto, _, version = build_request_data(WorkflowRunReadRequestDTOs, version=version)

        response = await self.client.post(
            endpoint=f"/workflows/{identifier}/run",
            body=input,
            headers={APIVersionHeader: build_version_header(WorkflowRunResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            query={"wait": wait, "namespace": namespace},
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)
