import os
import json
import subprocess

def main():
    template_repo_url = os.getenv('TEMPLATE_REPO_URL')
    template_variables_json = os.getenv('TEMPLATE_VARIABLES_JSON')
    template_variables = json.loads(template_variables_json)

    # Call cookiecutter with the environment variables
    subprocess.run(
        [
            'cookiecutter', 
            '--no-input', 
            '--output-dir', 
            './generated',
            template_repo_url
        ], 
        env={**os.environ, **template_variables}
    )

if __name__ == "__main__":
    main()
