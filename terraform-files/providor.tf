provider "aws" {
  region  = "us-east-1"
  profile = "default"

  assume_role {
    role_arn = "arn:aws:iam::992382853618:role/admin-access"
  }