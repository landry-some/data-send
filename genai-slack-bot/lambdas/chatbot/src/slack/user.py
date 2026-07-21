import requests, json
from typing import List
from lambdas.chatbot.src.slack.slack_oauth import get_env_var
from lambdas.chatbot.src.util.logging_config import LOGGER

def get_user_info(user_id: str):
    """
    Create new slack channel

    Args:
        channel_name (str): channel name to be created
        is_private (bool): if the channel is private

    Raises:
        ValueError: response is not ok
    """
    url = 'https://slack.com/api/users.info'
    payload = {
        'user': user_id
    }

    headers = {
        'Authorization': f'Bearer {get_env_var("BOT_OAUTH_TOKEN")}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=60)
    response.raise_for_status()
    response_data = response.json()
    
    print(response_data)
    
    if response.status_code == 200 and response_data.get("ok", False):
        user_info = response_data['user']
        
        LOGGER.info("User info for user id '%s' is %s", user_id, user_info)
        return user_info
    else:
        raise ValueError('Error encountered %s', response_data['error'])