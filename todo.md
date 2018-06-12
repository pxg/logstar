PR Rename app.py as api.py
PR improve API content headers (change DB field)
PR improve webapp content JSON
PR improve webapp content JSON
PR to bump requirements

Ability to click on one of the items
That's all link on load more

v1.0
Pretty print JSON on details page
Write blog article
Refine README

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