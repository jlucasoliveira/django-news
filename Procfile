release: python manage.py migrate
web: gunicorn newspaper_project.wsgi:application --bind 0.0.0.0:$PORT