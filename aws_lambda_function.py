import json
import os
import random
import string
import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3 = boto3.client('s3')

def generate_password(length=12):
    """Generate a random password with specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def lambda_handler(event, context):
    try:
        # Parse the body from API Gateway event
        body = event.get('body')
        if body:
            try:
                data = json.loads(body)
            except Exception:
                data = {}
        else:
            data = {}

        # Get password length from request, default to 12 if not specified
        password_length = data.get('length', 12)
        password = generate_password(password_length)

        # Prepare response
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({
                'password': password,
                'length': password_length
            })
        }
        return response

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({'error': str(e)})
        } 