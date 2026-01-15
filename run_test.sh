#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
source venv/Scripts/activate

# Run test suite
pytest

# If all tests pass, exit with code 0
exit 0
