# django-book-management

Application with book management API, registration API and sending email.
Used stack: *Django*, *MySQL*, *Redis*, *Celery*.

## Install

Install `django-book-management` from source:

    git clone https://github.com/omka0708/django-book-management
    cd django-book-management

You should have `.env` file at the */django-book-management* folder.

Environment file `.env` should contain:
    
    DJANGO_SECRET_KEY = <django secret key>
    DB_NAME = "books"
    DB_USER = "root"
    DB_PASSWORD = <your password>
    DB_HOST = "db"
    DB_PORT = "3306"
    EMAIL_HOST_USER = <gmail from which come letters>
    EMAIL_HOST_PASSWORD = <gmail application password>
    REDIS_LOCATION = 'redis://redis:6379'

Get django secret key [here](https://djecrety.ir/).

## Run

Run this command at the working directory */django-book-management*:

    docker compose up --build

## Create superuser
Database already have superuser `root:omka2061`.
If you want to create your superuser, use:

    docker exec -it books-django python manage.py createsuperuser

> Don't use Git Bash on windows for this command, use PowerShell

## Register API
### Register
#### Request

    POST http://localhost:8000/api/auth/register

#### With body like 

    {
        "username": "new_username",
        "email": "new@email.com",
        "password": "new_password"
    }
    
#### Response

    {
        "user": {
            "id": 15,
            "username": "new_username",
            "email": "new@email.com",
            "date_joined": "2023-11-25T02:58:37.994469+03:00"
        },
        "token": "6f627a65ea6f8b0a026dcf2c694789200ca957d9e1d04e4ac15139d131bacb6e"
    }
    
After successful register user get welcome mail.

### Login
#### Request

    POST http://localhost:8000/api/auth/login
    
#### With body like 

    {
        "username": "some_username",
        "password": "some_password"
    }

#### Response
##### Login successful

    {
        "user": {
            "id": 1,
            "username": "some_username",
            "email": "some@mail.com",
            "date_joined": "2023-11-23T18:12:11.118703+03:00"
        },
        "token": "ef2c958736e7585acf92abcdefa61dbac902agtcr4a397f18fe53af080815b"
    }
    
##### Login unsuccessful

    {
        "non_field_errors": [
            "Неверный логин или пароль."
        ]
    }

### Logout
#### Request

    POST http://localhost:8000/api/auth/logout
    
#### With header

    Authorization: Token b19f9643fe03a3afc1d9c4d48271366a16bb50deb3fcf984e9c8c5e9523ce54b
    
It will clear token from database.

### Get current user (Token required)
#### Request

    GET http://localhost:8000/api/user

#### Response

    {
        "id": 1,
        "username": "root",
        "email": "mcscare12@gmail.com",
        "date_joined": "2023-11-23T18:12:11.118703+03:00"
    }

### Get all users (only for admins)
#### Request

    GET http://localhost:8000/api/users

### Get specific user (only for admins)
#### Request

    GET http://localhost:8000/api/<int:pk>

## Books API
### Get all books / Create book or many books (Token required)
#### Request

    GET/POST http://localhost:8000/api/books
    
#### With body like (if POST)

    {
        "title": "Clara Callan",
        "author": "Richard Bruce Wright",
        "year": 2001,
        "ISBN": "2005018",
    }

### Get, change or delete book (Token required)
#### Request

    GET/PUT/PATCH/DELETE http://localhost:8000/api/books/<int:pk>

#### With body like (if PUT, PATCH)

    {
        "title": "Classical Mythology",
        "author": "Mark P. O. Morford",
        "year": 2002,
        "ISBN": "195153448",
    }

#### Response

    {
        "id": 1,
        "title": "Classical Mythology",
        "author": "Mark P. O. Morford",
        "year": 2002,
        "ISBN": "195153448",
        "created_at": "2023-11-24T20:35:39.261763+03:00",
        "updated_at": "2023-11-24T20:50:18.313911+03:00"
    }

