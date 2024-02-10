from flowdapt_sdk._compat import validate_model
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.utils import build_version_header, build_request_data
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.dto import V1Alpha1SystemStatus

ResourceType = "system"

SystemStatusRequestDTOs = {
    "v1alpha1": (None, V1Alpha1SystemStatus),
}
SystemStatusResponse = V1Alpha1SystemStatus


class SystemAPI(BaseAPI):
    """
    SystemAPI provides methods for interacting with the Flowdapt System API.

    It is not intended to be instantiated directly. Instead, it should be accessed
    via an instance of FlowdaptSDK.
    """
    async def status(self, version: str | None = None) -> SystemStatusResponse:
        """
        Get the status of the Flowdapt system.

        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The response from the status endpoint.
        :rtype: SystemStatusResponse
        """
        response_dto, _, version = build_request_data(SystemStatusRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/status",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return validate_model(response_dto, response.content)
