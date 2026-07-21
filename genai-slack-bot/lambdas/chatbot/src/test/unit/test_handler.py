"""Simple test case for Python reference app"""
import unittest
from unittest.mock import patch, MagicMock
import lambdas.chatbot.src.handler as handler

# Tests for small individual pieces of code
class TestChatbotPython(unittest.TestCase):
    """A simple class for unit test"""

    @patch("lambdas.chatbot.src.handler.LOGGER")
    @patch("lambdas.chatbot.src.handler.post_slack_message")
    def test_handler(self, mock_post_slack_message, mock_logger):
        """
        Test chatbot handler
        """
        # Define a mock event that matches the expected structure
        mock_event = {
            "event": {
                "channel": "C1234567890",
                "text": "Hi there!",
            }
        }

        # Mock the behavior of LOGGER
        mock_logger.info = MagicMock()
        mock_logger.error = MagicMock()

        # Mock the post_slack_message function
        mock_post_slack_message.return_value = None

        # Call the handler with the mock event
        handler.handle(mock_event, None)

        # Assert that post_slack_message was called with the correct parameters
        mock_post_slack_message.assert_called_once_with(
            handler.bot_oauth_token, 
            "C1234567890", 
            "this is echo bot: Hi there!"
        )

        # Assert that LOGGER.info was called correctly
        mock_logger.info.assert_any_call("Event triggered")
        mock_logger.info.assert_any_call("Sending data '%s'", "this is echo bot: Hi there!")

        # Assert that LOGGER.error was not called
        mock_logger.error.assert_not_called()
