import logging

def configure_logging():
    # Remove all existing handlers
    for handler in logging.getLogger().handlers[:]:
        logging.getLogger().removeHandler(handler)

    formatter = logging.Formatter('[%(levelname)s]  [%(asctime)s]  %(message)s')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

LOGGER = configure_logging()
