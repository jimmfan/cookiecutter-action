# Cookiecutter Action

This GitHub Action generates a project structure using a Cookiecutter template, allowing for dynamic inputs to customize the generated project. It's designed to streamline the setup of new projects by automating the creation process with predefined or custom Cookiecutter templates.

## Features

- **Dynamic Inputs**: Specify template variables directly through workflow inputs.
- **Flexible Template Sources**: Use any Cookiecutter template repository URL.
- **Customizable Output**: Define the output directory for the generated project structure.

## Prerequisites

Before you use this action, you'll need the following in your repository:
- A GitHub repository where you intend to use this action.
- The inputs list below.
- JSON file with the cookiecutter template variables

## Inputs

This action supports the following inputs:
- `workflow_token`: (Required) The github token with workflow write access (Required for editing .github/workflow templates)
- `template_var_path`: (Required) The JSON path containing all the Cookiecutter template variables.
- `template_directory`: (Optional) Relative path within the repository to the template directory. Default is the repository root.
- `output_directory`: (Optional) Output directory for the generated project. Defaults to the current working directory.

## Usage
Create a json file in your repo that matches with template cookiecutter.json file.  

# Example JSON for basic-python
```json
{   
    "project_name": "test_project",
    "author": "jimmfan",
    "email": "jimmmfan@github.com",
    "python_version": "3.10"
}
```

To use this action in your workflow, add the following step to your `.github/workflows/your-workflow.yml`:
{% raw %}
```yaml
name: Generate Project Structure

on:
  workflow_dispatch:
    inputs:
      template_directory:
        description: 'Relative path within the repository to the template directory'
        required: true    
      template_var_path:
        description: 'JSON path containing all the template variables'
        required: true
      workflow_token:
        description: 'Github token with workflow access'
        required: true

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
        workflow_token: ${{ secrets.WORKFLOW_TOKEN }}
        template_var_path: ${{ github.event.inputs.template_var_path }}
        template_directory: ${{ github.event.inputs.template_directory }}
        
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
{% endraw %}        