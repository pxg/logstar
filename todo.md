# Immediate

0. Install from master on Github
1. Install venv from scratch. Flask threaded=True test
2. Rename example_app.py to request.py and external_lib_request in examples folder
3. Run server with gunicorn or uwsgi
4. Example server

---

Listen to Tool

---

1. Load more on app (add pagination to the API)
2. Run app using package command
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

Have pytest automatically run httpbin
Add CircleCI. Could use https://hub.docker.com/r/citizenstig/httpbin/
Use Python type annotations
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions
Do all logging using python logging to avoid issues with DB writing blocking