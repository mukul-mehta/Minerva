# Minerva
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

[![Build Status](https://travis-ci.org/mukul-mehta/Minerva.svg?branch=master)](https://travis-ci.org/mukul-mehta/Minerva)

Minerva - A one-stop destination for everything Movie/TV Show Related!
Created as part of Software Engineering Lab (CS29006) during my 4th semester (Spring 2020) - The semester that never was. 



### Common Backend for Minerva

.
├── app
│   ├── \_\_init\_\_.py
│   ├── main
│   │   ├── config.py
│   │   ├── controller
│   │   │   ├── auth_controller.py
│   │   │   ├── post_controller.py
│   │   │   └── user_controller.py
|   |   ├── logging_config.py
│   │   ├── models
│   │   │   ├── movie.py
│   │   │   └── user.py
│   │   ├── service
│   │   │   ├── auth_helper.py
│   │   │   ├── movie_service.py
│   │   │   └── user_service.py
│   │   └── util
│   │       └── dto.py
│   └── test
│       └── base.py
|── .env
├── manage.py
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt

Collect all similar endpoints in the `app/controller` folder. Use different files for logically dissimilar endpoints.

NOTE: Most of the general config is loaded into the environment from the .env file which should be created from the provided .env.template



## Setting up the project locally

Please use pipenv.

To install pipenv run `pip install pipenv`.

Use a separate virtual environment by running `pipenv shell --three` and then run `pipenv install` to install dependencies.

NOTE: Run `pipenv install --dev` to install all dependencies including development.

## Adding new dependencies

To install a new dependency, use `pipenv install <pkg-name>`. This will update Pipfile and Pipfile.lock

NOTE: use the flag `--dev` if it is a development dependency.

To upgrade a package, use `pipenv install --selective-upgrade <pkg-name>`.

Whenever a new dependency is added, be sure to run

```shell
pip freeze > requirements.txt
```

Mention dependency change in the commit message.

## Using Makefile

We serve most of the common commands collected in a Makefile.

### Initial installation

```shell
make install
```

### Run tests

```shell
make tests
```

### Run server (not recommended for Production)

```shell
make run
```

## Run all commands at once

```shell
make all
```



## Docker Container

To build the container, make sure that the Dockerfile is present and run `docker build -t minerva:latest .`

To run the application from the docker container, run `docker run minerva ARG` where `ARG` can be `db`, `run, test`, `shell` or `runserver`.

For more information, run `docker run common-backend --help`.



## Setting up DB Migrations  

### First Time With Flask-Migrate

If this is the first time that flask-migrate is being installed or run alongside existing database, use the 
following command to create a head stamp in your database:<br>
`python manage.py db stamp head`  



If the `migrations` folder doesn't exist, use the following command before the above command. 

`python manage.py db init`

### Applying Schema Update On Existing Database

It is recommended to perform Database upgrades, whenever database schema is updated, using the below commands:<br>
`python manage.py db upgrade`  

### Removing Last Schema Update On Existing Database

Remove the last database update using the below commands:<br>
`python manage.py db downgrade`  

### Updating Schema

Whenever a database model's schema is update, run the following command to generate migrations for it.<br>
`python manage.py db migrate`