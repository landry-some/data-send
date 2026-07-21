from genosclient import ApiClient, Configuration, DelegateModeApi, Environment
from typing import Dict, Any, AsyncGenerator
from abc import ABC
from contextlib import asynccontextmanager


class DelegateModeApiBuilder(ABC):
    @classmethod
    def build(cls, metadata: Dict[str, Any]) -> DelegateModeApi:
        env = metadata.get("env", "e2e")
        configuration = Configuration(env=Environment[env])
        # configuration object is optional here, if you don't provide, it will use e2e url
        api_client = ApiClient(configuration=configuration, is_async=False)
        return DelegateModeApi(api_client)

    @classmethod
    @asynccontextmanager
    async def abuild(
        cls, metadata: Dict[str, Any]
    ) -> AsyncGenerator[DelegateModeApi, None]:
        env = metadata.get("env", "e2e")
        configuration = Configuration(env=Environment[env])
        async with ApiClient(configuration=configuration, is_async=True) as api_client:
            api_client = api_client
            yield DelegateModeApi(api_client)