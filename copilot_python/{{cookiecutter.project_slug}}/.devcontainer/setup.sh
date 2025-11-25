#!/bin/bash
set -e

git config --global user.email "{{ cookiecutter.email }}"
git config --global user.name "{{ cookiecutter.author }}"
git config --global --add safe.directory "${containerWorkspaceFolder}"
