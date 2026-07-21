import unittest
from unittest.mock import patch, MagicMock
import logging
from lambdas.chatbot.src.util.logging_config import configure_logging, LOGGER

class TestConfigureLogging(unittest.TestCase):
    """Tests for the configure_logging function"""

    @patch("logging.getLogger")
    def test_configure_logging(self, mock_get_logger):
        """
        Test the configure_logging function
        """
        # Mock logger object
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Call the configure_logging function
        logger = configure_logging()

        # Check that the function returns the correct logger
        self.assertEqual(logger, mock_logger)

        # Check that removeHandler was called for each existing handler
        # self.assertTrue(mock_logger.removeHandler.called)

        # Check that setLevel was called with logging.INFO
        mock_logger.setLevel.assert_called_with(logging.INFO)

        # Check that StreamHandler was added
        self.assertEqual(len(mock_logger.addHandler.call_args_list), 1)
        handler = mock_logger.addHandler.call_args_list[0][0][0]
        self.assertIsInstance(handler, logging.StreamHandler)

        # Check that the formatter is set correctly
        self.assertIsInstance(handler.formatter, logging.Formatter)
        self.assertEqual(handler.formatter._fmt, '[%(levelname)s]  [%(asctime)s]  %(message)s')
