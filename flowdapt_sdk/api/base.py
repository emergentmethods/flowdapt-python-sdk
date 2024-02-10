from flowdapt_sdk.client import APIClient


class BaseAPI:
    def __init__(self, client: APIClient) -> None:
        self.client = client
