import requests, json
from typing import List
from lambdas.chatbot.src.slack.slack_oauth import get_env_var
from lambdas.chatbot.src.util.logging_config import LOGGER

def delete_channel(channel_id: str):
    """
    Create new slack channel

    Args:
        channel_id (str): channel id to delete

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/conversations.archive'
    payload = {
        'channel': channel_id
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
    
    LOGGER.info("channel (%s) removal success!", channel_id)

def get_channel_id_from_name(channel_name: str):
    """
    Get channel id from channel name

    Args:
        channel_name (str): channel name to be created

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/conversations.list'
    payload = {}

    headers = {
        'Authorization': f'Bearer {get_env_var("BOT_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    
    print(response_data)
    if response_data.get("ok", False):
        channels = response_data.get('channels', [])
        channel_id = None
        for channel in channels:
            if channel['name'] == channel_name:
                channel_id = channel['id']
                break 
            
        LOGGER.info("Channel id of %s is %s", channel_name, channel_id)
        return channel_id
    else:
        raise ValueError('Error encountered %s', response_data['error'])

def create_new_channel(channel_name: str, is_private: bool = False):
    """
    Create new slack channel

    Args:
        channel_name (str): channel name to be created
        is_private (bool): if the channel is private
        
    Returns:
        channel_id: new channel id on success

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/conversations.create'
    payload = {
        'name': channel_name,
        'is_private': is_private,
    }

    headers = {
        'Authorization': f'Bearer {get_env_var("BOT_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    
    print(response_data)
    if response_data.get("ok", False):
        channel_id = response_data['channel']['id']
        
        LOGGER.info("New channel '%s'(%s) is created", channel_name, channel_id)
        return channel_id
    else:
        raise ValueError('Error encountered %s', response_data['error'])
    
def invite_users(channel_id: str, user_ids: List[str]):
    """
    Delete slack messsage from the channel

    Args:
        channel_id (str): channel id
        message_id (str): message id to delete

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/conversations.invite'
    payload = {
        'channel': channel_id,
        'users': ','.join(user_ids),
    }

    headers = {
        'Authorization': f'Bearer {get_env_var("BOT_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    
    print(response_data)
    
    if "error" in response_data:
        raise ValueError('Error encountered %s', response_data['error'])
    
    LOGGER.info("Users are successfully invited to %s channel", channel_id)