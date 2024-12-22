provider "aws" {
    region = "us-east-1"
}

resource "aws_ecr_repository" "my_repository" {
    name                 = "eitan-lior-ecr"
    image_tag_mutability = "MUTABLE"
    image_scanning_configuration {
        scan_on_push = true
    }
}