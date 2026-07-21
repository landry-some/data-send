from pprint import pprint

from genosclient import DelegateModeRequest

tmp_hdrs = {**headers}
# using different asset alias as it is configured as Originating asset alias in AI Workbench for the exp id
tmp_hdrs["jsguru_originating_assetalias"] = "jsguru.data.mlplatform.genosorchestrator"


def invoke_delegate_mode_post():
    # Create an instance of the API class
    api_instance = DelegateModeApiBuilder.build(metadata)
    req = DelegateModeRequest(
        message={
            "id": "1234",
            "timestamp": 121231,
            "content": "How to set up quickbooks?",
            "role": "customer",
        },
        accepted_renderers=[{"type": "FRF", "version": "1.0.0"}],
    )

    api_response = api_instance.invoke_delegate_mode_post(
        jsguru_experience_id="7ece8c59-987a-4c0a-a75b-657cd41280b4",
        delegate_mode_request=req,
        _headers=tmp_hdrs,
    )

    pprint(f"DelegateModeApi->invoke_delegate_mode_post: ")
    pprint(api_response)


async def ainvoke_delegate_mode_post():
    # Create an instance of the API class
    async with DelegateModeApiBuilder.abuild(metadata) as api_instance:
        try:
            req = DelegateModeRequest(
                message={
                    "id": "1234",
                    "timestamp": 121231,
                    "content": "How to set up quickbooks?",
                    "role": "customer",
                },
                accepted_renderers=[{"type": "FRF", "version": "1.0.0"}],
            )

            api_response = await api_instance.ainvoke_delegate_mode_post(
                jsguru_experience_id="7ece8c59-987a-4c0a-a75b-657cd41280b4",
                delegate_mode_request=req,
                _headers=tmp_hdrs,
            )

            pprint(f"DelegateModeApi->invoke_delegate_mode_post: ")
            pprint(api_response)
        except ApiException as e:
            print("DelegateModeApi->invoke_delegate_mode_post: %s\n" % e)