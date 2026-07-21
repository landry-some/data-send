"""
This module handles greetings.
"""

from datetime import datetime
from slack_sdk import WebClient

from lambdas.chatbot.src.util.logging_config import LOGGER
from lambdas.chatbot.src.slack.message import post_bot_message, delete_user_message
from lambdas.chatbot.src.slack.channel import (
    create_new_channel,
    invite_users,
)
from lambdas.chatbot.src.slack.user import get_user_info
from lambdas.chatbot.src.renderer.simulation_selector import display_simulation_types
from lambdas.chatbot.src.renderer.mkdwn import header_renderer


def starter_controller(event, userClient: WebClient, botClient: WebClient):  # pylint: disable=unused-argument
    """
    Main handler for the request

    Args:
        event: Event is expected to be populated by SQS. event['event'] will have the following:
            channel - channel id of the sender
            user - user id of the sender
            text - text of the block
            bot_profile - bot detail
        context: Default Value
    """
    LOGGER.info("Event triggered: %s", event)
    
    channel_id = event["event"]["channel"]
    user_text = event["event"]["text"]
    message_id = event["event"]["ts"]
    user_id = event["event"]["user"]

    try:
        if user_text == "chatbot":
            # Delete user message
            delete_user_message(userClient, channel_id, message_id)

            msg = display_simulation_types()
            post_bot_message(botClient, channel_id, msg)

        elif user_text == "new":
            # create new channel and determine channel name
            user_info = get_user_info(botClient, user_id)

            curr_time = datetime.now().strftime("%y%m%d%H%M%S")
            new_channel_name = f"cs-{user_info['name']}-{curr_time}"

            # now create new channel
            new_channel_id = create_new_channel(botClient, new_channel_name)
            invite_users(botClient, new_channel_id, [user_id])

            # display welcome msg
            msg = header_renderer("Welcome to the AI chat")
            post_bot_message(botClient, new_channel_id, msg)

    except Exception as err:
        LOGGER.error(err)

