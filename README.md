# journal
An exxampole of how to build a saas project using django

* [x] dependencies
* [x] Django Initialisation
* [ ] Configure via django-environ
* [ ] Configure web server
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





