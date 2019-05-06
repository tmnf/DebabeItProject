#!/bin/bash

python manage.py makemigrations forum
python manage.py sqlmigrate forum 0001
python manage.py migrate