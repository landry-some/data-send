import unittest
from unittest.mock import patch, MagicMock
import os
from lambdas.chatbot.src.slack.slack_oauth import get_bot_oauth_token 

class TestGetBotOAuthToken(unittest.TestCase):
    """Tests for the get_bot_oauth_token function"""

    @patch.dict(os.environ, {"ENVIRONMENT": "local", "BOT_OAUTH_TOKEN": "local_token"})
    def test_get_bot_oauth_token_local(self):
        """
        Test getting OAuth token in local environment
        """
        token = get_bot_oauth_token()
        self.assertEqual(token, "local_token")

    @patch.dict(os.environ, {"ENVIRONMENT": "production", "SECRET_NAME": "my_secret"})
    @patch('lib.clients.secrets_manager.SecretsClient.get_secrets')
    def test_get_bot_oauth_token_production(self, mock_get_secrets):
        """
        Test getting OAuth token in production environment
        """
        # Mock the behavior of SecretsClient
        mock_get_secrets.return_value = {"app_secret": "production_token"}

        token = get_bot_oauth_token()
        self.assertEqual(token, "production_token")
        
        # Verify that SecretsClient was initialized and get_secrets was called with the correct secret name
        mock_get_secrets.assert_called_once_with(secret_name="my_secret")

    @patch.dict(os.environ, {"ENVIRONMENT": "unknown"})
    def test_get_bot_oauth_token_unknown_environment(self):
        """
        Test handling of unknown environment
        """
        with self.assertRaises(ValueError) as context:
            get_bot_oauth_token()
        
        self.assertEqual(str(context.exception), "Unknown environment. Set ENVIRONMENT to 'local' or 'production'.")