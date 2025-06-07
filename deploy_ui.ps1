# Get the bucket name from Terraform output
$bucketName = "password-generator-ui"

# Upload index.html to S3
Write-Host "Uploading index.html to S3..."
aws s3 cp index.html "s3://$bucketName/index.html" --content-type "text/html"

Write-Host "UI deployment complete!"
Write-Host "You can access the UI at: http://$bucketName.s3-website-us-east-1.amazonaws.com" 