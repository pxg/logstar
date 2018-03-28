# Live server set-up

1. Run on port 80. Install Nginx with reverse proxy
2. Set-up Gunicorn to run with supervisor or similar

---

0. Better error message if LOGSTAR_DB_URL is missing
1. Move db.py functions
2. Load more on app (add pagination to the API)
3. Run the app from the package (make sure non-python files are included by installing from a Github URL with requirements.txt in fresh virtual environment)
4. Set-up on server (EC2/Heroku)
5. Publish to Pypi
6. Integrate with project for calling Monzo and Google sheets API
7. Create intialization/installation command
8. Make sure it works for put and delete requests
9. Clean installation of Repo to make sure instructions are good
10. Make serialization function smarter. TDD

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