#!/bin/bash
# HIPAA Compliance Dashboard Deployment Script
# Version: 2.1.4

echo "=== Deploying HIPAA Compliance Dashboard ==="
echo "Environment: $1"
echo "Release Date: $(date)"

# Install dependencies
pip install -r requirements.txt

# Set environment config
case $1 in
  dev)
    export STREAMLIT_SERVER_PORT=8502
    export ENV_LABEL="Development"
    ;;
  staging)
    export STREAMLIT_SERVER_PORT=8501
    export ENV_LABEL="Staging"
    ;;
  prod)
    export STREAMLIT_SERVER_PORT=8500
    export ENV_LABEL="Production"
    # Add production firewall rules if needed
    ;;
  *)
    echo "Usage: $0 {dev|staging|prod}"
    exit 1
    ;;
esac

echo "Starting $ENV_LABEL environment on port $STREAMLIT_SERVER_PORT..."
streamlit run app.py --server.port $STREAMLIT_SERVER_PORT
