import os
import json
from cookiecutter.main import cookiecutter

template_repo_url = 'https://github.com/jimmfan/cookiecutter-action.git' 
template_directory = os.getenv('TEMPLATE_DIRECTORY')

# Create template dictionary from env variables
extra_context = {
    key: os.getenv(key) for key in [
        'project_name', 
        'author', 
        'email', 
        'python_version',
        'terraform_org',
  ]
}

# Call cookiecutter with the loaded context and template directory
cookiecutter(
    template_repo_url,
    no_input=True,
    checkout='main', 
    extra_context=extra_context,
    directory=template_directory,
    output_dir='.'
)