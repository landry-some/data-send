import unittest
from unittest.mock import patch, Mock
import requests
from lambdas.chatbot.src.slack.http_handler import post_slack_message

class TestPostSlackMessage(unittest.TestCase):
    @patch('requests.post')
    def test_post_slack_message_success(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ok": True}
        mock_post.return_value = mock_response
        
        bot_token = 'xoxb-fake-bot-token'
        channel_id = 'C01234567'
        message = 'Hello, world!'
        
        # Act
        post_slack_message(bot_token, channel_id, message)
        
        # Assert
        mock_post.assert_called_once_with(
            'https://slack.com/api/chat.postMessage',
            json={'channel': channel_id, 'text': message},
            headers={
                'Authorization': f'Bearer {bot_token}',
                'Content-Type': 'application/json',
            },
            timeout=60
        )

    @patch('requests.post')
    def test_post_slack_message_http_error(self, mock_post):
        # Arrange
        mock_post.side_effect = requests.exceptions.HTTPError("HTTP error occurred")
        
        bot_token = 'xoxb-fake-bot-token'
        channel_id = 'C01234567'
        message = 'Hello, world!'
        
        # Act & Assert
        with self.assertRaises(requests.exceptions.HTTPError):
            post_slack_message(bot_token, channel_id, message)
    
    @patch('requests.post')
    def test_post_slack_message_api_error(self, mock_post):
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ok": False, "error": "channel_not_found"}
        mock_post.return_value = mock_response
        
        bot_token = 'xoxb-fake-bot-token'
        channel_id = 'C01234567'
        message = 'Hello, world!'
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            post_slack_message(bot_token, channel_id, message)
        
        self.assertIn('channel_not_found', str(context.exception))
