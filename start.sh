pip3 install -r requirements.txt
python3 manage.py migrate --noinput
# python3 manage.py runserver 0.0.0.0:8000
~/.local/bin/gunicorn myapp.wsgi -b=0.0.0.0:8000 --daemon

