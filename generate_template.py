import os
import json
import sys
from cookiecutter.main import cookiecutter

# Load JSON context from a file
extra_context = json.loads(os.getenv('TEMPLATE_JSON_VARIABLES', '{}')) 
template_repo_url = os.getenv('TEMPLATE_REPO_URL')
template_directory = os.getenv('TEMPLATE_DIRECTORY', '.')  # Default to '.'
output_directory = os.getenv('OUTPUT_DIRECTORY', '.')  # Default to '.'

print(f"extra_context type: {type(extra_context)}")
print(f"extra_context content: {extra_context}")

# Call cookiecutter with the loaded context and optional template directory
cookiecutter(
    template_repo_url,
    no_input=True,
    extra_context=extra_context,
    directory=template_directory,
    output_dir=output_directory
)