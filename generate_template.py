import os
import json
import sys
from cookiecutter.main import cookiecutter

# Load JSON context from a file
with open('context.json', 'r') as file:
    extra_context = json.load(file)

template_repo_url = os.getenv('TEMPLATE_REPO_URL')
template_directory = os.getenv('TEMPLATE_DIRECTORY', '.')  # Default to '.'
output_directory = os.getenv('OUTPUT_DIRECTORY', '.')  # Default to '.'

# Call cookiecutter with the loaded context and optional template directory
cookiecutter(
    template_repo_url,
    no_input=True,
    extra_context=extra_context,
    directory=template_directory,
    output_dir=output_directory
)