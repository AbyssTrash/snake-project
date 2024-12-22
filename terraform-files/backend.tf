terraform {
  backend "s3" {
    bucket         = "terraformfilesep"          # Your S3 bucket
    key            = "state/terraform.tfstate" # Path within the bucket for the state file
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}