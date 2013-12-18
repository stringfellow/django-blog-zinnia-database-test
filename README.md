To demonstrate the failure:

- make a virtualenv
- activate it
- create a database called `zinnia_test` on localhost's database (or edit `zinnia_test/settings.py`)
- run runme.sh

What happens is that the tests pass and then the database fails to get destroyed, resulting in this message:

    (zinnia_test)➜  zinnia_test  ./runme.sh
    Creating test database for alias 'default'...
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.311s

    OK
    Destroying test database for alias 'default'...
    DatabaseError: database "test_zinnia_test" is being accessed by other users
    DETAIL:  There are 1 other session(s) using the database.

This has been tested on 3 separate Apple computers.
