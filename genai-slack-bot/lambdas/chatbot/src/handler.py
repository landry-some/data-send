"""
This module handles greetings.
"""

from dotenv import load_dotenv
import json

load_dotenv()

from slack_sdk import WebClient
from lambdas.chatbot.src.util.config import get_env_var

from lambdas.chatbot.src.util.logging_config import LOGGER
from lambdas.chatbot.src.util.common import event_parser
from lambdas.chatbot.src.controller.chat import chat_controller
from lambdas.chatbot.src.controller.starter import starter_controller

botClient = WebClient(token=get_env_var("BOT_OAUTH_TOKEN"))
userClient = WebClient(token=get_env_var("USER_OAUTH_TOKEN"))


def handle(event, context):  # pylint: disable=unused-argument
    """
    Main handler for the request

    Args:
        event: Event is expected to be populated by SQS. event['event'] will have the following:
            channel - channel id of the sender
            user - user id of the sender
            bot_profile - bot detail
        context: Default Value
    """
    LOGGER.info("Event triggered: %s", event)
    
    path = event.get("pathParameters", {}).get("proxy", 'chat')
    event = event_parser(event)
    
    # for subscribe purpose in slack setting
    if "challenge" in event:
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "body": json.dumps({"challenge": event["challenge"]}),
        }
    
    if "bot_profile" not in event["event"]:
        # chat_controller(event, botClient)
        
        # starter_controller(event, userClient, botClient)
        if path == 'chat':
            chat_controller(event, botClient)
        
        elif path == 'starter':
            starter_controller(event, userClient, botClient)
    
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps({"message": "ok"}),
    }
