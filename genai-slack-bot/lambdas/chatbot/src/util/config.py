import os

from lib.clients.secrets_manager import SecretsClient
from lambdas.chatbot.src.util.logging_config import LOGGER

def get_env_var(name):
    """
    Get the value of env variable

    Raises:
        ValueError: in case of token not found

    Returns:
        str: slack oauth token
    """
    
    environment = os.getenv("ENVIRONMENT", "local")
    LOGGER.info("environment '%s'", environment)

    if environment == "local":
        return os.environ.get(name)
    elif 'pr' in environment:
        secret_session = SecretsClient()  # Initialize your secrets client
        secret_token = secret_session.get_secrets(secret_name=os.environ.get("SECRET_NAME"))[name]
        return secret_token
    else:
        raise ValueError("Unknown environment. Set ENVIRONMENT to 'local' or 'production'.")
