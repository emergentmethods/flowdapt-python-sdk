from typing import Union
from uuid import UUID

from flowdapt_sdk._compat import validate_model, model_dump
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.dto.configs import (
    V1Alpha1ConfigResourceCreateRequest,
    V1Alpha1ConfigResourceCreateResponse,
    V1Alpha2ConfigResourceCreateRequest,
    V1Alpha2ConfigResourceCreateResponse,
    V1Alpha1ConfigResourceUpdateRequest,
    V1Alpha1ConfigResourceUpdateResponse,
    V1Alpha1ConfigResourceReadResponse,
)
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.utils import (
    build_request_data,
    build_version_header,
)

ResourceType = "config"

ConfigCreateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1ConfigResourceCreateRequest,
        V1Alpha1ConfigResourceCreateResponse,
    ),
    "v1alpha2": (
        V1Alpha2ConfigResourceCreateRequest,
        V1Alpha2ConfigResourceCreateResponse,
    )
}
ConfigUpdateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1ConfigResourceUpdateRequest,
        V1Alpha1ConfigResourceUpdateResponse,
    ),
}
ConfigReadRequestDTOs = {
    "v1alpha1": (None, V1Alpha1ConfigResourceReadResponse),
}

ConfigReadResponse = V1Alpha1ConfigResourceReadResponse
ConfigCreateRequest = Union[
    V1Alpha1ConfigResourceCreateRequest,
    V1Alpha2ConfigResourceCreateRequest,
]
ConfigCreateResponse = Union[
    V1Alpha1ConfigResourceCreateResponse,
    V1Alpha2ConfigResourceCreateResponse,
]
ConfigUpdateRequest = V1Alpha1ConfigResourceUpdateRequest
ConfigUpdateResponse = V1Alpha1ConfigResourceUpdateResponse


class ConfigsAPI(BaseAPI):
    """
    The ConfigsAPI class provides methods for interacting with the Flowdapt Configs API.

    It is not intended to be instantiated directly. Instead, it should
    be accessed via an instance of FlowdaptSDK.
    """
    async def list_configs(self, version: str | None = None) -> list[ConfigReadResponse]:
        """
        List all configs.

        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: A list of configs.
        :rtype: list[ConfigReadResponse]
        """
        response_dto, _, version = build_request_data(ConfigReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/configs/",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return [validate_model(response_dto, data) for data in response.content]

    async def create_config(
        self,
        data: ConfigCreateRequest | dict,
        version: str | None = None
    ) -> ConfigCreateResponse:
        """
        Create a new config.

        :param data: The data for the new config.
        :type data: ConfigCreateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The new config.
        :rtype: ConfigCreateResponse
        """
        response_dto, data, version = build_request_data(
            ConfigCreateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.post(
            endpoint="/configs/",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return validate_model(response_dto, response.content)

    async def get_config(
        self,
        identifier: str | UUID,
        version: str | None = None
    ) -> ConfigReadResponse:
        """
        Get a config by its identifier.

        :param identifier: The identifier of the config.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The config.
        :rtype: ConfigReadResponse
        """
        response_dto, _, version = build_request_data(ConfigReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint=f"/configs/{identifier}",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def update_config(
        self,
        identifier: str | UUID,
        data: ConfigUpdateRequest | dict,
        version: str | None = None
    ) -> ConfigUpdateResponse:
        """
        Update a config by its identifier.

        :param identifier: The identifier of the config.
        :type identifier: str | UUID
        :param data: The data for the updated config.
        :type data: ConfigUpdateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The updated config.
        :rtype: ConfigUpdateResponse
        """
        response_dto, data, version = build_request_data(
            ConfigUpdateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.put(
            endpoint=f"/configs/{identifier}",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def delete_config(self, identifier: str | UUID, version: str | None = None) -> None:
        """
        Delete a config by its identifier.

        :param identifier: The identifier of the config.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: None
        """
        response_dto, _, version = build_request_data(ConfigReadRequestDTOs, version=version)

        response = await self.client.delete(
            endpoint=f"/configs/{identifier}",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)
