release: python manage.py makemigrations --hallinfo
release: python manage.py migrate --no-input

web: gunicorn Eventhall.wsgi