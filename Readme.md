# JDD Community Backend

## How to start development

```bash
$ # create virtual environment
$ mkvirtualenv jdd_community_backend
$ cd jdd_community_backend

$ # install requirements
$ pip install -r requirements.txt

$ # Set up django
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## To Do

* [x] Set up settings and admin display
* [ ] Set up homepage and blog mechanism front end
* [ ] Deploy to VPS
* [ ] Set up CICD