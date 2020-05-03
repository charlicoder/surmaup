
# adduser mamun

# usermod -aG sudo surmaup

# apt update

# apt install ufw

# ufw app list

# ufw allow OpenSSH

# ufw enable

# ufw status

# cp -r ~/.ssh /home/sammy

# chown -R sammy:sammy /home/sammy/.ssh


$ ssh mamun@your_server_ip

$ sudo apt update

$ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl


==========
$ sudo -u postgres psql

postgres# CREATE DATABASE surmaupdb;

postgres# CREATE USER surmaupdb_user WITH PASSWORD 'Surmaupdb@2020';

postgres# ALTER ROLE surmaupdb_user SET client_encoding TO 'utf8';

postgres# ALTER ROLE surmaupdb_user SET default_transaction_isolation TO 'read committed';

postgres# ALTER ROLE surmaupdb_user SET timezone TO 'UTC';

postgres# GRANT ALL PRIVILEGES ON DATABASE surmaupdb TO surmaupdb_user;

================

$ sudo -H pip3 install --upgrade pip

$ sudo apt-get install python3-venv

