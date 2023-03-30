#!/bin/sh

export PYTHONPATH:=$(shell pwd)/avito

run_admin:
	python avito/manage.py runserver

parse:
	python avito/manage.py parse_avito

makemigrations:
	python avito/manage.py makemigrations

migrate:
	python avito/manage.py migrate

cd %ProgramFiles%\PostgreSQL\14\bin\
psql.exe -h 127.0.0.1 -U postgres -W
CREATE DATABASE severcart WITH ENCODING='UTF8' OWNER=postgres CONNECTION LIMIT=-1 template=template0;

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}


# my.cnf
[client]
database = severcart #NAME
user = postgres #USER
password = postgres #PASSWORD
default-character-set = utf8