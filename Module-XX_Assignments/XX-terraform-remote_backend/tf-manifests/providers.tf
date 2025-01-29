/* For configuring TF script with remote backend, create below resources:
   1. S3 Bucket | In the any region
   2. DynamoDB with Partition key=LockID 
*/

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.41.0"
    }
  }
  backend "s3" {
    bucket         = "s3bucketnamefortfstate"
    key            = "prod.terraform.tfstate"
    dynamodb_table = "tf-state-info-table"
    region         = "us-east-1"
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "default"
}
