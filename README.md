# surmaup TODO's
Surmaup


[Unit]
Description=gunicorn daemon
Requires=gcorn_charlicoder.socket
After=network.target

[Service]
User=charli
Group=www-data
WorkingDirectory=/home/charli/django_projects/charlicoder.com
ExecStart=/home/charli/django_projects/charlicoder.com/venv_charlicoder/bin/gunicorn \
          --access-logfile - \
          --workers 2 \
          --bind unix:/run/gcorn_charlicoder.sock \
          charlicoder.][]:application

[Install]
WantedBy=multi-user.target
