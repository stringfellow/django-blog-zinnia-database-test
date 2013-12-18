#!/bin/bash
pip install -r requirements.txt
createdb -h localhost zinnia_test
python manage.py test blog

