#!/bin/bash

# activate the virtual environment
. ./venv/Scripts/activate

# run the test suite
python3 -m pytest test_app.py

# set exit code from pytest
EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi