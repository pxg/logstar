get_pagination_num()

1. Move db.py functions
2. Load more on app (add pagination to the API)
3. Run the app from the package change includes? Change readme command?
4. Publish to Pypi
5. Integrate with project for calling Monzo and Google sheets API
6. Create intialization/installation command
7. Make sure it works for put and delete requests
8. Clean installation of Repo to make sure instructions are good
9. Make serialization function smarter. TDD

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