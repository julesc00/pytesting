Django and Pytest tutorial


I. Running pytest and coverage:

pytest --cov==. # To run in the current folder or

pytest --cov==my_project app_name/tests/

pytest --cov=. --cov-report=html