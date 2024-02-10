from uuid import UUID

from flowdapt_sdk._compat import validate_model, model_dump
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.utils import build_version_header, build_request_data
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.dto import (
    V1Alpha1TriggerRuleResourceCreateRequest,
    V1Alpha1TriggerRuleResourceCreateResponse,
    V1Alpha1TriggerRuleResourceUpdateRequest,
    V1Alpha1TriggerRuleResourceUpdateResponse,
    V1Alpha1TriggerRuleResourceReadResponse,
)

ResourceType = "trigger_rule"
TriggerRuleCreateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1TriggerRuleResourceCreateRequest,
        V1Alpha1TriggerRuleResourceCreateResponse,
    ),
}
TriggerRuleUpdateRequestDTOs = {
    "v1alpha1": (
        V1Alpha1TriggerRuleResourceUpdateRequest,
        V1Alpha1TriggerRuleResourceUpdateResponse,
    ),
}
TriggerRuleReadRequestDTOs = {
    "v1alpha1": (None, V1Alpha1TriggerRuleResourceReadResponse),
}

TriggerRuleCreateRequest = V1Alpha1TriggerRuleResourceCreateRequest
TriggerRuleCreateResponse = V1Alpha1TriggerRuleResourceCreateResponse
TriggerRuleUpdateRequest = V1Alpha1TriggerRuleResourceUpdateRequest
TriggerRuleUpdateResponse = V1Alpha1TriggerRuleResourceUpdateResponse
TriggerRuleReadResponse = V1Alpha1TriggerRuleResourceReadResponse


class TriggersAPI(BaseAPI):
    """
    TriggersAPI class provides methods for interacting with the Flowdapt Triggers API.

    It is not intended to be instantiated directly. Instead, it should be accessed
    via an instance of FlowdaptSDK.
    """
    async def list_triggers(self, version: str | None = None) -> list[TriggerRuleReadResponse]:
        """
        List all triggers.

        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: A list of triggers.
        :rtype: list[TriggerRuleReadResponse]
        """
        response_dto, _, version = build_request_data(TriggerRuleReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/triggers/",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return [validate_model(response_dto, data) for data in response.content]

    async def create_trigger(
        self,
        data: TriggerRuleCreateRequest | dict,
        version: str | None = None,
    ) -> TriggerRuleCreateResponse:
        """
        Create a new trigger.

        :param data: The data for the new trigger.
        :type data: TriggerRuleCreateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The new trigger.
        :rtype: TriggerRuleCreateResponse
        """
        response_dto, data, version = build_request_data(
            TriggerRuleCreateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.post(
            endpoint="/triggers/",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return validate_model(response_dto, response.content)

    async def get_trigger(
        self,
        identifier: str | UUID,
        version: str | None = None
    ) -> TriggerRuleReadResponse:
        """
        Get a trigger by its identifier.

        :param identifier: The identifier of the trigger.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The trigger.
        :rtype: TriggerRuleReadResponse
        """
        response_dto, _, version = build_request_data(TriggerRuleReadRequestDTOs, version=version)

        response = await self.client.get(
            endpoint=f"/triggers/{identifier}",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def update_trigger(
        self,
        identifier: str | UUID,
        data: TriggerRuleUpdateRequest | dict,
        version: str | None = None,
    ) -> TriggerRuleUpdateResponse:
        """
        Update a trigger.

        :param identifier: The identifier of the trigger to update.
        :type identifier: str | UUID
        :param data: The data for the updated trigger.
        :type data: TriggerRuleUpdateRequest | dict
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The updated trigger.
        :rtype: TriggerRuleUpdateResponse
        """
        response_dto, data, version = build_request_data(
            TriggerRuleUpdateRequestDTOs,
            data=data,
            version=version
        )

        response = await self.client.put(
            endpoint=f"/triggers/{identifier}",
            body=model_dump(data),
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)

    async def delete_trigger(
        self,
        identifier: str | UUID,
        version: str | None = None,
    ) -> None:
        """
        Delete a trigger by its identifier.

        :param identifier: The identifier of the trigger to delete.
        :type identifier: str | UUID
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: None
        """
        response_dto, _, version = build_request_data(TriggerRuleReadRequestDTOs, version=version)

        response = await self.client.delete(
            endpoint=f"/triggers/{identifier}",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"identifier": identifier}
        )

        return validate_model(response_dto, response.content)
