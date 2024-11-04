# math_services
Math Services for BackStage

## Questions

1. Is this to be a purely public service (or is user authentication required)?
    - Right now I am going to assume that it is a public service

2. Should the Database (sqlite3 file) be included in the repo?
    - I don't think so
    - Need to add instructions on saving it / creating a new one

## Assumptions

1. Can use Python 3.12.7 (one of the latest versions of Python)
2. Can use Django 4.2 (one of the latest LTS versions of Django)
3. It is ok to not split out the Dev requirements into their own file

## Considerations

1. To make it easier to run: the django project was created in the root of the repo. It would usually be created in a subfolder, something like ./src.

## Tools and Packages

### Tools

1. pyenv 2.4.16 (only needed if python 3.12.7 is not the default python)
2. python 3.12.7

### Packages

1. Sqlite3 for the database
2. PyTest for unit testing
