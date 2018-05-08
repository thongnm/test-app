# Test - App Server

## Intall dependencies

```sh
pip3 install -r requirements.txt
```

## Migrate data

```sh
python3 manage.py migrate --noinput
```

## Create a database 
- Conect to Postgres database server
- Create a database

## Add environment variables

```sh
sudo tee -a /etc/environment << EOF
POSTGRES_HOSTNAME=[database host]
POSTGRES_USER=[database username]
POSTGRES_DB=[database name]
POSTGRES_PASSWORD=[database password]
DEFAULT_FILE_STORAGE=storages.backends.s3boto3.S3Boto3Storage
STATICFILES_STORAGE=storages.backends.s3boto3.S3Boto3Storage
MEDIA_URL=https://s3-ap-southeast-2.amazonaws.com/s3test/media/
STATIC_URL=https://s3-ap-southeast-2.amazonaws.com/s3test/static/
HOSTNAME=https://myapp.net
EOF
```

## Start server 

```sh
~/.local/bin/gunicorn myapp.wsgi -b=0.0.0.0:8000 --daemon
```
