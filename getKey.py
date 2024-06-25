import boto3
import json
from botocore.exceptions import ClientError


def get_secret(SecretName, access_id, secret_access_id):
    secret_name = SecretName
    region = "us-east-1"

    session = boto3.Session(
        aws_access_key_id=access_id,
        aws_secret_access_key=secret_access_id,
        region_name=region
    )
    client = session.client(
        service_name='secretsmanager',
        region_name=region
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    
    return secret

