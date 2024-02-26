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
- `template_directory`: (Optional) Relative path within the repository to the template directory. Default is the repository root.
- `template_var_path`: (Required) The JSON path containing all the Cookiecutter template variables.
- `workflow_token`: (Required) The github token with workflow write access (Required for editing .github/workflow templates)

## Usage
Create a json file in your repo that matches with template cookiecutter.json file.  

# Example JSON for basic_python
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
  push:

env:
  template_directory: 'basic_python'
  template_var_path: 'cookiecutter_inputs.json'
  
jobs:
  generate_template:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    steps:
    - name: Create Cookiecutter Template
      uses: jimmfan/cookiecutter-action@main
      with:
        template_directory: ${{ env.template_directory }}
        template_var_path: ${{ env.template_var_path }}
        workflow_token: ${{ secrets.WORKFLOW_TOKEN }}
        
    - name: Create and Push to Branch
      run: |
        BRANCH_NAME=${{ github.ref_name }}
        # Configure Git with the provided environment variables
        git config user.name "${{ env.GIT_USER_NAME }}"
        git config user.email "${{ env.GIT_USER_EMAIL }}"
        git checkout $BRANCH_NAME
        git add .
        git commit -m "Generate project structure with Cookiecutter"
        git push -u origin $BRANCH_NAME
      env:
        GIT_USER_NAME: "GitHub Actions"
        GIT_USER_EMAIL: "actions@github.com"
        
```
{% endraw %}        