variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "password_length" {
  description = "Length of the generated password"
  type        = number
  default     = 12
} 