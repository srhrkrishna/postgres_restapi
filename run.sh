#!/bin/sh
cat /etc/hosts
# migrate db, so we have the latest db schema
su -c "python manage.py migrate"
# start development server on public ip interface, on port 8000
su -c "python manage.py runserver 0.0.0.0:8000"