import requests
import json
from lambdas.chatbot.src.slack.slack_oauth import get_env_var
from lambdas.chatbot.src.util.logging_config import LOGGER
from typing import List

def delete_user_message(channel_id: str, message_id: str):
    """
    Delete slack messsage from the channel

    Args:
        channel_id (str): channel id
        message_id (str): message id to delete

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/chat.delete'
    payload = {
        'channel': channel_id,
        'ts': message_id,
    }

    headers = {
        'Authorization': f'Bearer {get_env_var("USER_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    if "error" in response_data:
        raise ValueError('Error encountered %s', response_data['error'])
    
    LOGGER.info("User message '%s' is removed from channel '%s'", message_id, channel_id)

def post_bot_message(channel_id: str, message: List[object]):
    """
    Post slack messsage to the channel

    Args:
        channel_id (str): channel id to post
        message (str): message to post

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/chat.postMessage'
    payload = {
        'channel': channel_id,
        'blocks': message,
    }

    headers = {
        'Authorization': f'Bearer {get_env_var("BOT_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    if "error" in response_data:
        raise ValueError('Error encountered %s', response_data['error'])
    
    LOGGER.info("Bot posted message successfully to channel '%s", channel_id)