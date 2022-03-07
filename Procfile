release: python manage.py migrate
web: gunicorn japan.wsgi --log-file=-
worker: celery --app japan worker -l info