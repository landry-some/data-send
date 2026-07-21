"""
This module handles greetings.
"""
from slack_sdk import WebClient

from lambdas.chatbot.src.util.logging_config import LOGGER
from lambdas.chatbot.src.slack.message import post_bot_message
from lambdas.chatbot.src.renderer.mkdwn import markdown_renderer

def chat_controller(event, botClient: WebClient):  # pylint: disable=unused-argument
    """
    AI Chat handler

    Args:
    """
    LOGGER.info("Event triggered: %s", event)

    channel_id = event["event"]["channel"]
    user_text = event["event"]["text"]

    try:
        msg = markdown_renderer(user_text)
        post_bot_message(botClient, channel_id, msg)

    except Exception as err:
        LOGGER.error(err)