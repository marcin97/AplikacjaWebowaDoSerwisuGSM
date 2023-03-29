# Aplication for GSM Service

Application for managment gsm service

## Technologies

Project is created with:

* Python version: 3.10
* Django version: 3.2

## Run application
```
$ docker-compose up --build -d
```

## Run tests

```
$ docker-compose up --build -d
$ docker exec -it inz-web-1 bash
$ python manage.py test hardware/tests
$ python manage.py test main/tests
$ python manage.py test utility/tests
```