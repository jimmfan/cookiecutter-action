import os
import json
import subprocess

def main():
    template_repo_url = os.getenv('TEMPLATE_REPO_URL')
    template_variables_json = os.getenv('TEMPLATE_VARIABLES_JSON')
    template_directory = os.getenv('TEMPLATE_DIRECTORY', '.')  # Default to '.'
    output_directory = os.getenv('OUTPUT_DIRECTORY', '.')  # Default to '.'
    template_variables = json.loads(template_variables_json)

    print(type(template_variables))  # Should be <class 'dict'>
    print(template_variables)
    print(template_variables['project_name'])  # Test access

    command = ['cookiecutter', '--no-input', '--output-dir', output_directory]
    if template_directory != '.':
        command += ['--directory', template_directory]
    command.append(template_repo_url)

    # Execute the cookiecutter command with the specified environment variables
    subprocess.run(command, env={**os.environ, **template_variables})

if __name__ == "__main__":
    main()