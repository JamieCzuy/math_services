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
4. The types for the different values in the response are not defined. Here are my assumptions:
    "datetime" - String (representing a Timezone aware timestamp)
    "value" - Integer
    "number" - Integer
    "occurrences" - Integer
    "last_datetime" - String (representing a Timezone aware timestamp)

5. There are no requirements around error handling so here are my assumptions:
    1. For the /difference endpoint:
        If n is not given  or n > 100 or n is not an integer return a 400 Bad Request with a message about n is required and required to be an integer between 0 and 100.

6. Assuming last_requested can be None, representing a number that has never been requested. Means can't use `auto_now`.

## Considerations

1. To make it easier to run: the django project was created in the root of the repo. It would usually be created in a subfolder, something like ./src.

2. For the difference, n is guaranteed to be an integer that is greater than 0 and less than or equal to 100 - so we can pre-compute the values and just have 100 rows in the database.

3. Persistance - for the API we need:
    1. What the first services require:
        1. The number passed in
        2. The solution (we could recalculate but why bother if we are already pulling other info)
        3. Occurrences (number of times n has been requested)
        4. The timestamp from the last time n was requested
    2. Optional 1 adds:
        1. More that just one number being passed in

4. These don't feel like class based views. But maybe since we are going to pre-compute the values maybe they are. For now let's go with functional based views.

5. For all text that a user might see we could be using Django utils translation - gettext_lazy (often mapped to "_"). Not going to do that now, just a thought.

## Tools and Packages

### Tools

1. pyenv 2.4.16 (only needed if python 3.12.7 is not the default python)
2. python 3.12.7

### Packages

1. Sqlite3 for the database
2. Django REST Framework
3. PyTest for unit testing
