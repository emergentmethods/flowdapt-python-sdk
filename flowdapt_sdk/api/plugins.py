from typing import AsyncIterator

from flowdapt_sdk._compat import validate_model
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.utils import build_version_header, build_request_data
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.dto import V1Alpha1Plugin, V1Alpha1PluginFiles

PluginResourceType = "plugin"
PluginFileResourceType = "plugin.files"

PluginRequestDTOs = {
    "v1alpha1": (None, V1Alpha1Plugin),
}
PluginFileRequestDTOs = {
    "v1alpha1": (None, V1Alpha1PluginFiles),
}

PluginResponse = V1Alpha1Plugin
PluginFileResponse = V1Alpha1PluginFiles


class PluginsAPI(BaseAPI):
    """
    PluginsAPI provides methods for interacting with the Flowdapt Plugins API.

    It is not intended to be instantiated directly. Instead, it should be accessed
    via an instance of FlowdaptSDK.
    """
    async def get_plugin(self, plugin_name: str, version: str | None = None) -> PluginResponse:
        """
        Get a plugin information by name.

        :param plugin_name: The name of the plugin to get.
        :type plugin_name: str
        :param version: The version of the plugin to get.
        :type version: str
        :return: The response from the plugin endpoint.
        :rtype: PluginResponse
        """
        response_dto, _, version = build_request_data(PluginRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/plugin/{plugin_name}",
            headers={APIVersionHeader: build_version_header(PluginResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"plugin_name": plugin_name},
        )

        return validate_model(response_dto, response.content)

    async def list_plugins(self, version: str | None = None) -> list[PluginResponse]:
        """
        List all plugins.

        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: A list of plugins.
        :rtype: list[PluginResponse]
        """
        response_dto, _, version = build_request_data(PluginRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/plugin/",
            headers={APIVersionHeader: build_version_header(PluginResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return [validate_model(response_dto, data) for data in response.content]

    async def list_plugin_files(
        self,
        plugin_name: str,
        version: str | None = None
    ) -> PluginFileResponse:
        """
        List all files for a plugin.

        :param plugin_name: The name of the plugin to get files for.
        :type plugin_name: str
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str | None
        :return: The response from the plugin files endpoint.
        :rtype: PluginFileResponse
        """
        response_dto, _, version = build_request_data(PluginFileRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/plugin/{plugin_name}/files",
            headers={APIVersionHeader: build_version_header(PluginFileResourceType, version)},
            accept=[(response_dto.__content_type__, 1.0)],
            params={"plugin_name": plugin_name},
        )

        return validate_model(response_dto, response.content)

    async def get_plugin_file(self, plugin_name: str, file_name: str) -> AsyncIterator[bytes]:
        """
        Download a file from a plugin.

        :param plugin_name: The name of the plugin to get the file from.
        :type plugin_name: str
        :param file_name: The name of the file to download.
        :type file_name: str
        :return: The content of the file.
        :rtype: AsyncIterator[bytes]
        """
        response = await self.client.get(
            endpoint="/plugin/{plugin_name}/files/{file_name}",
            accept=[("application/octet-stream", 1.0)],
            params={"plugin_name": plugin_name, "file_name": file_name},
            stream=True,
        )

        return response.content
