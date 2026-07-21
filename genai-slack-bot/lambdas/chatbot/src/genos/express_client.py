from genosclient import ApiClient, Configuration, ExpressModeApi, Environment
from typing import Dict, Any, AsyncGenerator
from abc import ABC
from contextlib import asynccontextmanager

class ExpressModeApiBuilder(ABC):
    @classmethod
    def build(cls, metadata: Dict[str, Any]) -> ExpressModeApi:
        env = metadata.get("env", "e2e")
        configuration = Configuration(env=Environment[env])
        # configuration object is optional here, if you don't provide, it will use e2e url
        api_client = ApiClient(configuration=configuration, is_async=False)
        return ExpressModeApi(api_client)

    @classmethod
    @asynccontextmanager
    async def abuild(
        cls, metadata: Dict[str, Any]
    ) -> AsyncGenerator[ExpressModeApi, None]:
        env = metadata.get("env", "e2e")
        configuration = Configuration(env=Environment[env])
        async with ApiClient(configuration=configuration, is_async=True) as api_client:
            api_client = api_client
            yield ExpressModeApi(api_client)