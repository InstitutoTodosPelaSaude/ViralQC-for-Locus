#!/bin/bash

# Configure viralQC datasets
set -eo pipefail
vqc get-nextclade-datasets --datasets-dir /usr/local/datasets
vqc get-blast-database --output-dir /usr/local/datasets

# Run health checks
python /app/healthchecks/healthcheck.py

# Check if the health check passed
if [ $? -eq 0 ]; then
  echo "Health checks passed. Starting Aplication..."

  uvicorn main:app --reload --host 0.0.0.0 --port 8000
else
  echo "Health checks failed. Exiting."
  exit 1
fi