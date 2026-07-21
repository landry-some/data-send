import logging
import time

from genosclient import PromptRequest
from genosclient.log_utils import getLogger

_logger: logging.Logger = getLogger(__name__)


def test_llmaccess_v1_with_prompt():
    # Create an instance of the API class
    api_instance = LLMAccessWithPromptVendingV1ApiBuilder.build(metadata)
    prompt_req = PromptRequest(
        prompt_input={
            "prompt_id": "example-prompt-id",
            "prompt_version": "4",
            "parameters": {
                "user_question": "How to do roth conversion in turbotax?",
                "user_name": "Gabe",
            },
        }
    )
    start = time.time()

    api_response = api_instance.llmaccess_v1_with_prompt(
        jsguru_experience_id=EXPERIENCE_ID,
        prompt_request=prompt_req,
        _headers=headers,
    )

    end = time.time()
    _logger.info(
        f"The response time: {(end - start)} LLMAccessWithPromptVendingV1Api->llmaccess_v1_with_prompt: "
    )
    _logger.info(api_response)


async def atest_llmaccess_v1_with_prompt():
    # Create an instance of the API class
    async with LLMAccessWithPromptVendingV1ApiBuilder.abuild(metadata) as api_instance:
        prompt_req = PromptRequest(
            prompt_input={
                "prompt_id": "example-prompt-id",
                "prompt_version": "4",
                "parameters": {
                    "user_question": "How to do roth conversion in turbotax?",
                    "user_name": "Gabe",
                },
            }
        )
        start = time.time()

        api_response = await api_instance.allmaccess_v1_with_prompt(
            jsguru_experience_id=EXPERIENCE_ID,
            prompt_request=prompt_req,
            _headers=headers,
        )

        end = time.time()
        _logger.info(
            f"The response time: {(end - start)} LLMAccessWithPromptVendingV1Api->llmaccess_v1_with_prompt: "
        )
        _logger.info(api_response)