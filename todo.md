# Immediate

0. Add extra fields into DB elapsed time. TDD
1. Recreate DB on start of test run
2. Integrate with project for calling Monzo and Google sheets API to check it really works
3. Build simple API and polling frontend

# Later

Script making an API request using async calls
Test with simple Salesforce library

# Tech

Have pytest automatically run httpbin
Add CircleCI
Add black formatter
Make into package
Use Python type annotations
Publish to Pypi
Check for compatibility with Celery, RQ, etc

# Enchancements

logstar_off function
logstar decorator for functions
Do all logging using python logging to avoid issues with DB writing blocking