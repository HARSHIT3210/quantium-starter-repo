#!/bin/bash

# Exit immediately if any command fails (except pytest, handled separately)
set -e

# Define the virtual environment path
VENV_PATH="./venv"

# Activate virtual environment
if [ -f "$VENV_PATH/bin/activate" ]; then
    source "$VENV_PATH/bin/activate"
elif [ -f "$VENV_PATH/Scripts/activate" ]; then
    # For Windows environments
    source "$VENV_PATH/Scripts/activate"
else
    echo "❌ Virtual environment not found at $VENV_PATH"
    exit 1
fi

echo "✅ Virtual environment activated."

# Run the tests using pytest
echo "🚀 Running test suite..."
pytest ./tests

# Capture exit code from pytest
TEST_RESULT=$?

# Handle result
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi
