from lambdas.chatbot.src.util.logging_config import LOGGER

def markdown_renderer(mkdwn: str):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": mkdwn
            }
        },
    ]
