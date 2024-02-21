# Cookiecutter Action

This GitHub Action generates a project structure using a Cookiecutter template, allowing for dynamic inputs to customize the generated project. It's designed to streamline the setup of new projects by automating the creation process with predefined or custom Cookiecutter templates.

## Features

- **Dynamic Inputs**: Specify template variables directly through workflow inputs.
- **Flexible Template Sources**: Use any Cookiecutter template repository URL.
- **Customizable Output**: Define the output directory for the generated project structure.

## Prerequisites

Before you use this action, you'll need:
- A GitHub repository where you intend to use this action.
- A Cookiecutter template repository URL.

## Inputs

This action supports the following inputs:

- `template_var_path`: (Required) The JSON path containing all the Cookiecutter template variables.
- `template_repo_url`: (Required) The Cookiecutter template git repository URL.
- `template_directory`: (Optional) Relative path within the repository to the template directory. Default is the repository root.
- `output_directory`: (Optional) Output directory for the generated project. Defaults to the current working directory.

## Usage

Create a json file in your repo that matches with template cookiecutter.json file.  

```json
{   
    "project_name": "test_project",
    "author": "jimmfan",
    "email": "jimmmfan@github.com",
    "python_version": "3.10"
}
```

To use this action in your workflow, add the following step to your `.github/workflows/your-workflow.yml` (this will get deleted):

```yaml
name: Generate Project Structure

on:
  workflow_dispatch:
    inputs:
      template_var_path:
        description: 'JSON path containing cookiecutter template variables'
        required: true
        default: 'cookiecutter_inputs.json'
      template_repo_url:
        description: 'Cookiecutter template git repository URL'
        required: true
        default: 'https://github.com/jimmfan/cookiecutter-action.git'
      template_directory:
        description: 'Relative path within the repository to the template directory'
        required: false
        default: 'template1'

jobs:
  generate_template:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    steps:
    - name: Checkout repo
      uses: actions/checkout@v2

    - name: Create Cookiecutter Template
      uses: jimmfan/cookiecutter-action@main
      with:
        template_var_path: ${{ github.event.inputs.template_var_path }}
        template_repo_url: ${{ github.event.inputs.template_repo_url }}
        template_directory: ${{ github.event.inputs.template_directory }}
    
    # Example pushing to a branch
    - name: Create and Push to Branch
      run: |
        BRANCH_NAME="generated-${{ github.run_id }}"
        # Configure Git with the provided environment variables
        git config user.name "${{ env.GIT_USER_NAME }}"
        git config user.email "${{ env.GIT_USER_EMAIL }}"
        git checkout -b $BRANCH_NAME
        git add .
        git commit -m "Generate project structure with Cookiecutter"
        git push -u origin $BRANCH_NAME
      env:
        GIT_USER_NAME: "GitHub Actions"
        GIT_USER_EMAIL: "actions@github.com"
```
        