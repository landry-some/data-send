#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

if [ -z "$VIRTUAL_ENV" ]; then
  echo "Please enable a python 3 virtual env"
  exit 1
fi

echo "Using virtualenv located in: $VIRTUAL_ENV"

echo -e "\n| --------------------- Running unit tests and coverage --------------------------- |"
cd "$REPO_DIR"
python -m pytest --cov-report xml:$coverageReport --cov=$covDir $testPath --junitxml=$testResults
echo -e "\n| --------------------- Unit tests and coverage completed ------------------------- |"
