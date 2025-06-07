# Create Lambda deployment packages
Compress-Archive -Path aws_lambda_function.py -DestinationPath aws_lambda_function.zip -Force
Compress-Archive -Path aws_lambda_function.py -DestinationPath aws_lambda_function.zip -Force
Write-Host "Created aws_lambda_function.zip and aws_lambda_function.zip successfully!" 