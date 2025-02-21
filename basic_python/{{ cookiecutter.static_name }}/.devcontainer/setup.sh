#!/bin/bash
set -e  # Exit if any command fails

# Update and install dependencies
sudo apt-get update
# Optional add apt-get commands
# sudo apt-get install -y tesseract-ocr mupdf mupdf-tools libmupdf-dev

# Configure Git
git config --global user.email "jimmfan@users.noreply.github.com"
git config --global user.name "jimmfan"
git config --global --add safe.directory "${containerWorkspaceFolder}"
