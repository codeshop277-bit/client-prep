import boto3
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()

def create_bedrock_client():
    region= 'ap-south1'
    aws_config = Config(
        connect_timeout=5,
        read_timeout=90,
        retries={
            "mode": "standard",
            "total_max_attempts": 4
        }
    )

    return boto3.client(
        "bedrock_runtime",
        region_name=region,
        config = aws_config
    )

# connect_timeout: Limits the time spent establishing a connection.
# read_timeout: Limits how long the client waits for the response.
# standard retry mode: Lets the AWS SDK retry eligible transient errors and throttling failures.
# total_max_attempts: Caps the total SDK attempts, including the original request.

def invoke_bedrock():
     response = client.converse(
            modelId=model_id,
            system=system,
            messages=messages,
            inferenceConfig={
                "maxTokens": 700,
                "temperature": 0.1,
            },
        )