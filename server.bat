@echo off

REM Set environment variable for this session
set DJANGO_ENV=development

REM Run Django development server
python manage.py runserver

pause
