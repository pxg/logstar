0. Load more on app

1. Publish to Pypi
2. Integrate with project for calling Monzo and Google sheets API
3. Create intialization/installation command
4. Make sure it works for put and delete requests
5. Clean installation of Repo to make sure instructions are good
6. Make serialization function smarter. TDD

# Live server set-up

Run on port 80. Install Nginx with reverse proxy
Set-up Gunicorn to run with supervisor or similar

# Later

Script making an API request using async calls
Test with simple Salesforce library

# Tech

Flask blueprint (app, UI)
Use config.py with Flask
Add CircleCI
Use Python type annotations
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions
Do all logging using python logging to avoid issues with DB writing blocking