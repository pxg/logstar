v1.0
0. Make sure it works for put and delete requests
1. Clean installation of Repo to make sure instructions are good
2. Style the app
3. Bump the version number
4. Write release blog article

v1.1+
Publish to Pypi
Integrate with project for calling Monzo and Google sheets API
Create intialization/installation command
Make serialization function smarter. TDD

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