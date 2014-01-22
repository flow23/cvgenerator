#!/bin/sh
cd /var/www/cvgenerator
python manage.py backup -d virtualenv/backups
