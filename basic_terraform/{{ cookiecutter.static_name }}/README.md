# Requirements
AWS
Terraform Cloud

# Example Usage
    # providers
    terraform {
        required_version = "~> 1.0"
        cloud {
            hostname     = "app.terraform.io"
            organization = "workspace-name"
            workspaces {
                name = "aws-python-lambda"
            }
        }
        required_providers {
            aws = {
            source  = "hashicorp/aws"
            version = "~> 5.0"
            }
        }
    }

    provider "aws" {
        allowed_account_ids     = [var.account_id]
        access_key              = var.access_key
        secret_key              = var.secret_key
        region                  = var.region
        skip_metadata_api_check = true
        default_tags {
            tags = {
                GitHubRepo = "aws-python-lambda"
                Workspace  = "aws-python-lambda"
            }
        }
    }

    # Example of lambda that has DynamoDB access
    module "lambda_dynamo_api" {
        source  = "app.terraform.io/workspace-name/lambda/aws"
        version = "0.0.11"

        lambda_name         = "lambda-name"
        handler             = "lambda.handler"
        account_id          = var.account_id
        region              = var.region
        runtime             = "python3.8"
        source_file         = "../path/to/lambda.py"

        # Optional DynamoDB access
        dynamodb_table_name = "example_dynamodb_table"

        # Optional Lambda Layers
        layers = [
            data.terraform_remote_state.workspace.outputs.layer1_arn,
            data.terraform_remote_state.workspace.outputs.layer2_arn
        ]

        # Optional Environmental Variables
        environment_variables = {
            region              = var.region
        }

        # Other Optional Arguments
        timeout                           = 3
        memory_size                       = 128
        log_retention_in_days             = 14
        provisioned_concurrent_executions = 20

        # Optional Tags
        tags = {
            Project = "project-name"
        }
    }

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | 2.4.0 |
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.23.1 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_log_group.lambda_log_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_iam_policy.iam_lambda_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_role.iam_role_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_lambda_function.lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_lambda_provisioned_concurrency_config.provisioned_concurrency_for_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_provisioned_concurrency_config) | resource |
| [archive_file.lambda_function](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |
| [aws_iam_policy_document.lambda_policy_document](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_id"></a> [account\_id](#input\_account\_id) | AWS Account ID | `number` | n/a | yes |
| <a name="input_cloudwatch_log_tags"></a> [cloudwatch\_log\_tags](#input\_cloudwatch\_log\_tags) | Additional map of tags for cloudwatch. Merged with the tags variable and assigned to cloudwatch log group resources. | `map(string)` | `{}` | no |
| <a name="input_dynamodb_table_name"></a> [dynamodb\_table\_name](#input\_dynamodb\_table\_name) | The name of the DynamoDB table that the lambda function needs access to.  If empty, DynamoDB policy will not be generated. | `string` | `""` | no |
| <a name="input_environment_variables"></a> [environment\_variables](#input\_environment\_variables) | Optional environment variables for the lambda function. Defaults to {} | `map(string)` | `{}` | no |
| <a name="input_handler"></a> [handler](#input\_handler) | Lambda Function entrypoint in your code.  For python, it will be the filename (module) and lambda function name.  ie. module.function | `string` | n/a | yes |
| <a name="input_lambda_name"></a> [lambda\_name](#input\_lambda\_name) | Name of lambda function | `string` | n/a | yes |
| <a name="input_layers"></a> [layers](#input\_layers) | List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function | `list(string)` | `null` | no |
| <a name="input_log_retention_in_days"></a> [log\_retention\_in\_days](#input\_log\_retention\_in\_days) | Specifies the number of days you want to retain log events in the specified log group. Valid values: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653, 0, and null. If you select 0, the events in the log group are always retained and never expire. Null will not create a log group | `number` | `null` | no |
| <a name="input_memory_size"></a> [memory\_size](#input\_memory\_size) | Amount of memory in MB your Lambda Function can use at runtime. Defaults to 128 | `number` | `128` | no |
| <a name="input_provisioned_concurrent_executions"></a> [provisioned\_concurrent\_executions](#input\_provisioned\_concurrent\_executions) | Amount of capacity to allocate. If specified, it will overwrite the publish argument in aws\_lambda\_function resource to be true and create a new lambda version. Must be greater than or equal to 1 to create resource. If 0, resource will not be created. | `number` | `0` | no |
| <a name="input_publish"></a> [publish](#input\_publish) | Whether to publish creation/change as new Lambda Function Version. Defaults to false | `bool` | `false` | no |
| <a name="input_region"></a> [region](#input\_region) | n/a | `string` | `"us-east-1"` | no |
| <a name="input_runtime"></a> [runtime](#input\_runtime) | Identifier of the function's runtime. Defaults to python3.8. Valid Values: nodejs \| nodejs4.3 \| nodejs6.10 \| nodejs8.10 \| nodejs10.x \| nodejs12.x \| nodejs14.x \| nodejs16.x \| java8 \| java8.al2 \| java11 \| python2.7 \| python3.6 \| python3.7 \| python3.8 \| python3.9 \| dotnetcore1.0 \| dotnetcore2.0 \| dotnetcore2.1 \| dotnetcore3.1 \| dotnet6 \| nodejs4.3-edge \| go1.x \| ruby2.5 \| ruby2.7 \| provided \| provided.al2 \| nodejs18.x \| python3.10 \| java17 \| ruby3.2 \| python3.11 | `string` | `"python3.8"` | no |
| <a name="input_source_file"></a> [source\_file](#input\_source\_file) | File path of lambda function. ie. ../src/lambda | `string` | n/a | yes |
| <a name="input_tags"></a> [tags](#input\_tags) | A map of tags to assign to resources. | `map(string)` | `{}` | no |
| <a name="input_timeout"></a> [timeout](#input\_timeout) | Amount of time your Lambda Function has to run in seconds. Defaults to 3 | `number` | `3` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_arn"></a> [arn](#output\_arn) | Amazon Resource Name (ARN) identifying your Lambda Function. |
| <a name="output_invoke_arn"></a> [invoke\_arn](#output\_invoke\_arn) | ARN to be used for invoking Lambda Function from API Gateway - to be used in aws\_api\_gateway\_integration's uri. |
| <a name="output_name"></a> [name](#output\_name) | Unique name for your Lambda Function. |
| <a name="output_qualified_arn"></a> [qualified\_arn](#output\_qualified\_arn) | ARN identifying your Lambda Function Version (if versioning is enabled via publish = true). |
| <a name="output_qualified_invoke_arn"></a> [qualified\_invoke\_arn](#output\_qualified\_invoke\_arn) | Qualified ARN (ARN with lambda version number) to be used for invoking Lambda Function from API Gateway - to be used in aws\_api\_gateway\_integration's uri |
| <a name="output_version"></a> [version](#output\_version) | Latest published version of your Lambda Function. |
<!-- END_TF_DOCS -->