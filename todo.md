# Immediate

0. Run API using package command, and move to it's own directory
1. Move serialization function to it's own file and make smarter
2. Integrate with project for calling Monzo and Google sheets API to check it really works
3. Build frontend app which polls API
4. Create intialization/installation command
5. Make sure it works for put and delete requests

# Later

Script making an API request using async calls
Test with simple Salesforce library

# Tech

Have pytest automatically run httpbin
Add CircleCI. Could use https://hub.docker.com/r/citizenstig/httpbin/
Add black formatter
Make into package
Use Python type annotations
Publish to Pypi
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions
Do all logging using python logging to avoid issues with DB writing blocking