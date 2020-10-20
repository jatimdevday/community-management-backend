# JDD Community Backend

Di website ini memiliki target awal dan target akhir. Target awal adalah website ini akan membantu menampilkan event yang akan berjalan dan akan dilaksanakan oleh komunitas yang ada di jawa timur. Target akhir adalah nantinya website akan mengakomodir adanya komunitas di jawa timur seperti pembuatan komunitas baru. Untuk sementara kita berfokus pada target awal terlebih dahulu dengan ekspektasi selesai pengerjaan pada 27 november 2020.

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
