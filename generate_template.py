import os
import json
from cookiecutter.main import cookiecutter

# Load JSON context from a file
with open(os.getenv('TEMPLATE_VAR_PATH'), 'r') as f:
    extra_context = json.load(f)

template_repo_url = 'https://github.com/jimmfan/cookiecutter-action.git' 
template_directory = os.getenv('TEMPLATE_DIRECTORY', '.')  # Default to '.'

# Call cookiecutter with the loaded context and template directory
cookiecutter(
    template_repo_url,
    no_input=True,
    extra_context=extra_context,
    directory=template_directory,
    output_dir='.'
)