import base64
from pprint import pprint

from genosclient import ApiException, ExpressModeV2RequestMessage
from genosclient.genos_client import build_headers
from lambdas.chatbot.src.genos.express_client import ExpressModeApiBuilder

metadata = {
    "env": "e2e",
    "jsguru_originating_assetalias": "xxx"
}

EXPERIENCE_ID = "xxxxx"

headers = build_headers(metadata)


def chat_completion_example1():

    with open("test/test.jpg", "rb") as image_file:
        express_mode_chat_request = ExpressModeV2RequestMessage(
            llm_input={
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image"},
                            {"type": "text", "text": "Describe in great detail"},
                            {
                                "type": "image",
                                "inline_data": {
                                    "data": base64.b64encode(image_file.read()),
                                    "mime_type": "image/jpeg",
                                },
                            },
                        ],
                    }
                ],
                "model_parameters": {
                    "temperature": 0,
                    "max_tokens": 1000,
                },
            }
        )
        # Create an express mode api instance
        api_instance = ExpressModeApiBuilder.build(metadata)
        try:
            # Chat completion, Best for chatbot experience
            api_response = api_instance.chat_completion_v2(
                model_id="gemini-1.5-pro-preview-0409",
                jsguru_experience_id=EXPERIENCE_ID,
                express_mode_v2_request_message=express_mode_chat_request,
                _headers=headers,
            )
            print("The response of ExpressModeApi->chat_completion:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExpressModeApi->chat_completion: %s\n" % e)

def chat_completion_example2():

    express_mode_chat_request = ExpressModeV2RequestMessage(
        llm_input={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {
                    "role": "assistant",
                    "content": "The Los Angeles Dodgers won the World Series in 2020.",
                },
                {"role": "user", "content": "Where was it played?"},
            ],
            "model_parameters": {
                "temperature": 0,
                "max_tokens": 250,
            },
        }
    )
    # Create an express mode api instance
    api_instance = ExpressModeApiBuilder.build(metadata)
    try:
        # Chat completion, Best for chatbot experience
        api_response = api_instance.chat_completion_v2(
            model_id="gpt-35-turbo",
            jsguru_experience_id=EXPERIENCE_ID,
            express_mode_v2_request_message=express_mode_chat_request,
            _headers=headers,
        )
        print("The response of ExpressModeApi->chat_completion:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExpressModeApi->chat_completion: %s\n" % e)

async def achat_completion_example():

    express_mode_chat_request = ExpressModeV2RequestMessage(
        llm_input={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {
                    "role": "assistant",
                    "content": "The Los Angeles Dodgers won the World Series in 2020.",
                },
                {"role": "user", "content": "Where was it played?"},
            ],
            "model_parameters": {
                "temperature": 0,
                "max_tokens": 250,
            },
        }
    )
    # Create an express mode api instance
    async with ExpressModeApiBuilder.abuild(metadata) as api_instance:
        try:
            # Chat completion, Best for chatbot experience
            api_response = await api_instance.achat_completion_v2(
                model_id="gpt-35-turbo",
                jsguru_experience_id=EXPERIENCE_ID,
                express_mode_v2_request_message=express_mode_chat_request,
                _headers=headers,
            )
            print("The response of ExpressModeApi->chat_completion:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExpressModeApi->chat_completion: %s\n" % e)