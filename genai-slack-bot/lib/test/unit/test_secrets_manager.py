import unittest
from unittest.mock import patch, MagicMock
import json
import base64
import boto3
from botocore.exceptions import ClientError
from lambdas.chatbot.src.util.logging_config import LOGGER
from lib.clients.secrets_manager import SecretsClient

class TestSecretsClient(unittest.TestCase):
    """Tests for the SecretsClient class"""

    @patch('boto3.session.Session')
    def setUp(self, mock_session):
        """
        Set up the test case.
        """
        # Mock the boto3 session and client
        self.mock_session = mock_session
        self.mock_client = MagicMock()
        self.mock_session.return_value.client.return_value = self.mock_client
        self.client = SecretsClient(session=self.mock_session.return_value)

    @patch.object(LOGGER, 'error')
    def test_get_secrets_success_string(self, mock_logger):
        """
        Test retrieving secrets when SecretString is present.
        """
        secret_name = "test_secret"
        secret_value = {"app_secret": "test_token"}

        # Mock the get_secret_value response
        self.mock_client.get_secret_value.return_value = {
            "SecretString": json.dumps(secret_value)
        }

        # Call the method
        result = self.client.get_secrets(secret_name)

        # Assert the result
        self.assertEqual(result, secret_value)
        self.mock_client.get_secret_value.assert_called_once_with(SecretId=secret_name)
        mock_logger.assert_not_called()

    @patch.object(LOGGER, 'error')
    def test_get_secrets_success_binary(self, mock_logger):
        """
        Test retrieving secrets when SecretBinary is present.
        """
        secret_name = "test_secret"
        secret_value = {"app_secret": "test_token"}
        secret_binary = base64.b64encode(json.dumps(secret_value).encode('utf-8')).decode('utf-8')

        # Mock the get_secret_value response
        self.mock_client.get_secret_value.return_value = {
            "SecretBinary": secret_binary
        }

        # Call the method
        result = self.client.get_secrets(secret_name)

        # Assert the result
        self.assertEqual(result, secret_value)
        self.mock_client.get_secret_value.assert_called_once_with(SecretId=secret_name)
        mock_logger.assert_not_called()

    @patch.object(LOGGER, 'error')
    def test_get_secrets_client_error(self, mock_logger):
        """
        Test handling of ClientError exception.
        """
        secret_name = "test_secret"
        error_message = "Client error"
        self.mock_client.get_secret_value.side_effect = ClientError(
            {"Error": {"Message": error_message}}, "GetSecretValue"
        )

        # Call the method and assert that an exception is raised
        with self.assertRaises(ClientError):
            self.client.get_secrets(secret_name)

        # Check that the error was logged
        mock_logger.assert_called_once_with(self.mock_client.get_secret_value.side_effect)
        self.mock_client.get_secret_value.assert_called_once_with(SecretId=secret_name)