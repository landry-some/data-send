import base64
import json
import logging

import boto3
from botocore.exceptions import ClientError

from lambdas.chatbot.src.util.logging_config import LOGGER

class SecretsClient:
    def __init__(self, session=None):
        if session:
            self.session = session
        else:
            self.session = boto3.session.Session(region_name='us-west-2')
        self.secret = self.session.client('secretsmanager', region_name='us-west-2')

    def get_secrets(self, secret_name):
        """
        Function used get secret entry from AWS Secret Manager by secret name
        :params secret_name: ARN/Name of secret as string
        """
        try:
            response = self.secret.get_secret_value(SecretId=secret_name)

        except ClientError as e:
            LOGGER.error(e)
            raise e

        if 'SecretString' in response:
            secret = json.loads(response['SecretString'])
            return secret

        decoded_binary_secret = base64.b64decode(response['SecretBinary'])
        decoded_binary_secret = json.loads(decoded_binary_secret)

        return decoded_binary_secret
