from lambdas.chatbot.src.util.logging_config import LOGGER

def display_simulation_types():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Choose AI simulator:"
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Performance Simulator"
                    },
                    "value": "button_1",
                    "action_id": "button_click_1"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Chat Simulator"
                    },
                    "value": "button_2",
                    "action_id": "button_click_2"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Quick Quiz (Recall Challenge)"
                    },
                    "value": "button_3",
                    "action_id": "button_click_3"
                }
            ]
        }
    ]
