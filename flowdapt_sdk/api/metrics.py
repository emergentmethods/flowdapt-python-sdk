from datetime import datetime

from flowdapt_sdk._compat import validate_model
from flowdapt_sdk.api.base import BaseAPI
from flowdapt_sdk.constants import APIVersionHeader
from flowdapt_sdk.utils import (
    build_request_data,
    build_version_header,
)
from flowdapt_sdk.dto import V1Alpha1Metrics

ResourceType = "metrics"

MetricsRequestDTOs = {
    "v1alpha1": (None, V1Alpha1Metrics),
}
MetricsResponse = V1Alpha1Metrics


class MetricsAPI(BaseAPI):
    """
    MetricsAPI class provides methods for interacting with the Flowdapt Metrics API.

    It is not intended to be instantiated directly. Instead, it should be accessed
    via an instance of FlowdaptSDK.
    """
    async def metrics(
        self,
        name: str | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        max_length: int | None = None,
        version: str | None = None,
    ) -> MetricsResponse:
        """
        Get metrics from the Flowdapt API.

        :param name: The name of the metric to retrieve.
        :type name: str
        :param start_time: The start time for the metric data.
        :type start_time: datetime
        :param end_time: The end time for the metric data.
        :type end_time: datetime
        :param max_length: The maximum number of data points to return.
        :type max_length: int
        :param version: The version of the DTO to use. Defaults to the latest supported version.
        :type version: str
        :return: The response from the metrics endpoint.
        :rtype: MetricsResponse
        """
        response_dto, _, version = build_request_data(MetricsRequestDTOs, version=version)

        response = await self.client.get(
            endpoint="/metrics",
            headers={APIVersionHeader: build_version_header(ResourceType, version)},
            query={
                "name": name,
                "start_time": start_time,
                "end_time": end_time,
                "max_length": max_length,
            },
            accept=[(response_dto.__content_type__, 1.0)],
        )

        return validate_model(response_dto, response.content)
