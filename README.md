# Password Generator System

This system implements a serverless password generation service using AWS services. The system follows this flow:
1. API Gateway receives HTTP requests
2. Messages are sent to SQS
3. Lambda function processes the message and generates a random password
4. The password is published to an SNS topic
5. All activity is logged in CloudTrail

## Architecture

- **API Gateway**: HTTP API endpoint that receives requests
- **SQS**: Message queue for handling password generation requests
- **Lambda**: Python function that generates random passwords
- **SNS**: Topic for publishing generated passwords
- **CloudTrail**: Logging and monitoring of all AWS activity
- **S3**: Bucket for storing CloudTrail logs
- **Web UI**: Modern, responsive interface for generating passwords

## Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform installed
- Python 3.9 or later
- Web server (optional, for serving the UI)

## Setup

1. Initialize Terraform:
   ```bash
   terraform init
   ```

2. Create a ZIP file for the Lambda function:
   ```bash
   zip aws_lambda_function.zip aws_lambda_function.py
   ```

3. Apply the Terraform configuration:
   ```bash
   terraform apply
   ```

4. After deployment, update the `API_ENDPOINT` in `index.html` with your API Gateway endpoint URL.

## Usage

### Web UI
1. Open `index.html` in a web browser
2. Enter the desired password length (8-32 characters)
3. Click "Generate Password"
4. Use the "Copy" button to copy the generated password to your clipboard

### API
To generate a password programmatically, send a POST request to the API Gateway endpoint:
```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/prod/generate-password \
  -H "Content-Type: application/json" \
  -d '{"length": 16}'
```

The generated password will be published to the SNS topic. You can subscribe to the SNS topic to receive the passwords.

## UI Features

- Modern, responsive design using Tailwind CSS
- Password length customization
- Loading indicators
- Copy to clipboard functionality
- Error handling and user feedback
- Mobile-friendly interface

## Monitoring

All activity is logged in CloudTrail and stored in the S3 bucket. You can view the logs in the AWS CloudTrail console or directly in the S3 bucket.

## Security

- All AWS resources are created with least-privilege IAM policies
- CloudTrail logging is enabled for all regions
- S3 bucket versioning is enabled for CloudTrail logs
- Passwords are generated using cryptographically secure random number generation
- CORS headers are configured for secure API access

## Cleanup

To destroy all resources:
```bash
terraform destroy
``` 