terraform {
  required_version = "~> 1.0"
  cloud {
    hostname     = "app.terraform.io"
    organization = "{{ cookiecutter.terraform_org }}"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}