#!/bin/sh
python manage.py dumpdata --indent=4 cv > cv/fixtures/initial_data.json
python manage.py dumpdata --indent=4 generator > generator/fixtures/initial_data.json
