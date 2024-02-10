from __future__ import annotations
from typing import Optional

from flowdapt_sdk.client import APIClient
from flowdapt_sdk.api import (
    ConfigsAPI,
    TriggersAPI,
    WorkflowsAPI,
    MetricsAPI,
    SystemAPI,
    PluginsAPI,
)


class FlowdaptSDK:
    """
    The FlowdaptSDK class is the main entry point for interacting with the Flowdapt API.

    :param base_url: The base URL of the Flowdapt API.
    :param verify_ssl: Whether to verify the SSL certificate of the Flowdapt API.
    :param retries: The number of times to retry a request if it fails.
    :param timeout: The timeout for requests to the Flowdapt API.
    """
    def __init__(
        self,
        base_url: str,
        verify_ssl: bool = True,
        retries: int = 3,
        timeout: Optional[float] = None,
    ) -> None:
        self.client = APIClient(
            base_url=base_url,
            verify_ssl=verify_ssl,
            retries=retries,
            timeout=timeout,
        )

        self.configs = ConfigsAPI(self.client)
        self.triggers = TriggersAPI(self.client)
        self.workflows = WorkflowsAPI(self.client)
        self.metrics = MetricsAPI(self.client)
        self.system = SystemAPI(self.client)
        self.plugins = PluginsAPI(self.client)

    async def __aenter__(self) -> FlowdaptSDK:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.client.__aexit__(exc_type, exc, tb)

    async def close(self) -> None:
        """
        Close the FlowdaptSDK client.
        """
        await self.client.close()

    async def ping(self) -> dict:
        """
        Call the ping endpoint of the Flowdapt API.

        :return: The response from the ping endpoint.
        :rtype: dict
        """
        response = await self.client.get("/")
        return response.content
