v1.0
1. Update readme for react app development
2. Update readme for react app product build
3. Update readme for running react app in production
4. Pretty print JSON on details page
5. Write blog article
6. Rewrite README

v1.1+
Move this file to Github projects
Have all CSS, JS, etc local
Publish to Pypi
Reduce duplicated code in logger.py
Integrate with project for calling Monzo and Google sheets API
Create intialization/installation command
Make serialization function smarter. TDD

v1.2
Log using customer logger rather than monkey patching
Check errors due to lack of DB connection etc do not crash app

# Live server set-up

Run on port 80. Install Nginx with reverse proxy
Set-up Gunicorn to run with supervisor or similar

# Later

Script making an API request using async calls
Test with simple Salesforce library

# Tech

Flask blueprint (app, UI)
Use config.py with Flask
Use Python type annotations
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions