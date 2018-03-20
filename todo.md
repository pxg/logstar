# Immediate

0. Run API using package command
1. Move serialization function to it's own file
2. Create logger.py with main logging functions
3. Integrate with project for calling Monzo and Google sheets API to check it really works
4. Build frontend app which polls API

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