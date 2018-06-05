v1.0
0. Rewrite README
1. Write release blog article

v1.1+
Publish to Pypi
Reduce duplicated code in logger.py
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