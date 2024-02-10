# Flowdapt Python SDK

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flowdapt_sdk?style=flat-square)

This is the official Python SDK for the Flowdapt API. It provides a simple way to programmatically interact with Flowdapt in Python. It is asynchronous and uses `httpx` as the underlying HTTP client.

## Installation

```bash
pip install flowdapt_sdk
```

## Usage

```python
import asyncio
from flowdapt_sdk import FlowdaptSDK

async def main():
    async with FlowdaptSDK(base_url="http://localhost:8080/") as client:
        print(await client.ping())

        workflows = await client.workflows.list_workflows(version="v1alpha1")
        print(workflows)

        workflow = await client.workflows.get_workflow("my-workflow", version="v1alpha1")
        print(workflow)

        result = await client.workflows.run_workflow(
            identifier="my-workflow",
            input={"x": 5},
            wait=True,
            namespace="default",
            version="v1alpha1"
        )
        print(result)
```