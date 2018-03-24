# Immediate

0. Expand stand alone request page. Move JS to footer
1. Continually poll the API
2. Load more on the API (pagination)

3. Run API using package command, and move to it's own directory
4. Move serialization function to it's own file and make smarter
5. Integrate with project for calling Monzo and Google sheets API to check it really works
6. Create intialization/installation command
7. Make sure it works for put and delete requests
8. Clean installation of Repo to make sure instructions are good
9. Run the UI/API from the package (make sure non-python files are included by installing from a Github URL with requirements.txt)

# Later

Script making an API request using async calls
Test with simple Salesforce library

# Tech

Have pytest automatically run httpbin
Add CircleCI. Could use https://hub.docker.com/r/citizenstig/httpbin/
Use Python type annotations
Publish to Pypi
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions
Do all logging using python logging to avoid issues with DB writing blocking