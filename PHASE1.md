# Phase 1

# Acceptance criteria:
- Created DB with zero migration containing `plant` table with columns `name, id`
- main.py with endpoint `/` that prints `hello`
- `/plant/{name}` endpoint printing dictionary of plant with id and name

# Tasks
1) Create repository structure under `src/app/` directory [reference](https://github.com/pl88/plantapp/pull/13) - create directories with only `__init__.py` file inside
2) Create main.py containing only `/` endpoint
3) update makefile to run `src/app/main.py` and remove `src/main.py`
4) create schemas for plant endpoint
5) create settings.py file
6) create basePlant and Plant models
7) Create `session.py` file with `get_db()` method.
8) create repositories simillar to examples
9) Install alembic and create migration with current plant model
10) TASK FOR BOTH:
   1) `pip install ipython`
   2) call `ipython`
   3) through ipython try to import repository, plant model and add single plant to db
   4) We may do it on interactive session
11) Create endpoint (router) similar to example ot print plant record (dict of plant name and id). Add router to app
12) End of phase 1. Check if all have tests

# Phase2

# Acceptance criteria:
- Extend plant model for addiional fields
- Extend endpoint for plant/name
- Add endpoints for categories
- Add endpoint for list of plants
