# snes_games_api

Django REST API for the Super Nintendo PAL games library with user authentication

Includes

- title
- publisher
- developer
- release year
- region
- front cover images [https://github.com/Constuelo/pal-snes-covers](https://github.com/Constuelo/pal-snes-covers)

## Requirements

**Python 3.7**

**Django 2.2**

**Pipenv** for a virtual environment

## Installation

    git clone
    pipenv install
    pipenv shell
    python3 manage.py runserver

## How To

Navigate to the games api [http://127.0.0.1:8000/games/](http://127.0.0.1:8000/games/)

Filter using url query parameters

- ?id=
- ?release=
- ?region=
- ?publisher=
- ?developer=
- ?title=

Example using multiple filters [http://127.0.0.1:8000/games/?publisher=Namco&release=1993](http://127.0.0.1:8000/games/?publisher=Namco&release=1993)

## Schema

[http://127.0.0.1:8000/schema/](http://127.0.0.1:8000/schema/)
