rem export PYTHONPATH:=$(shell pwd)/avito
rem  .\Make srv
rem  .\Make reg
rem cd avito_parser_django/avito
echo off
SET PYTHONPATH:=$(shell pwd)/avito
GOTO %1

:srv
SET PYTHONPATH:=$(shell pwd)/avito
python I:\\pythonProjects\\avito_django_telebot\\avito_parser_django\\avito\\manage.py runserver

:reg
SET PYTHONPATH:=$(shell pwd)/avito
call python I:\\pythonProjects\\avito_django_telebot\\avito_parser_django\\avito\\manage.py !!!!_httpx_region_ORM
GOTO end

:mkmig
call python I:\\pythonProjects\\avito_django_telebot\\avito_parser_django\\avito\\manage.py makemigrations
GOTO end

:mig
python I:\\pythonProjects\\avito_django_telebot\\avito_parser_django\\avito\\manage.py migrate

:end