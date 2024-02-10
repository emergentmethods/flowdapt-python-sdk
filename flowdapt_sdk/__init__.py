# flake8: noqa
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from flowdapt_sdk.version import __version__
from flowdapt_sdk.sdk import FlowdaptSDK

__all__ = (
    "__version__",
    "FlowdaptSDK",
)
