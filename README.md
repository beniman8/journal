# journal
An exxampole of how to build a saas project using django

* [x] dependencies
* [x] Django Initialization
* [x] Configure via django-environ
* [x] Configure web server
* [ ] testing / coverage
* [ ] CI - Continuous Integration 
* [x] pre-commit
* [ ] Django modeling
* [ ] Heroku  .. might no use this I prefer linode and aws


## setup on windows

```
virtualenv Env

Env\Scripts\activate
pip install -r requirements-dev.txt 
pip-compile requirements.in
pip install -r requirements.txt

django-admin startproject core .

python manage.py runserver

pre-commit run -a
pre-commit install
```

## Extra Files explainations

### Makefile

makefile is use to create shortcut command to get the terminal to execute other commands.

example:

instead of typing python manage.py in your terminal.You can just set it the make file so that it can run it,
when you type make  or make local  or make deploy

example of the way to create shortcuts in a makefile
```
.PHONY: local

local:
	py manage.py runserver

```





