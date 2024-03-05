release: python manage.py migrate
web: gunicorn core.wsgi --workers 2 --log-file -