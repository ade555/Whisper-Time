# WhisperTime - Databases

## Introduction

In development mode, WhisperTime makes use of the default SQLite database provided by Django. This section will take you through the process of changing it to a different database such as MySQL or PostgreSQL.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Using a PostgreSQL Database](#using-a-postgresql-database)
- [Using a MySQL Database](#using-a-mysql-database)

## Prerequisites

To successfully complete this guide, you must have gone through the [installation process](../README.md#getting-started) exlained earlier.

## Using a PostgreSQL Database

To use a PostgreSQL database, follow these steps:

1. [Download and install PostgreSQL](https://www.postgresql.org/download/) on your machine.

2. Install the Python adapter for PostgreSQL:

```
pip install psycopg2
```

3. Create a database for the project
[creating a new database in postgresql's pgadmin4](./images/create%20new%20postgres%20db.png)

4. Navigate to the settings file at `core/settings.py` and replace the database settings with the following:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username', # set this to your database username/owner
        'PASSWORD': 'your_password', # the password for the user 
        'HOST': 'localhost', # Set to the appropriate host if you don't have PostgreSQL on your local machine
        'PORT': '', # Leave it empty to use the default port (5432)
    }
}

```

5. Migrate your models to create the tables in PostgreSQL:

```
python manage.py migrate
```

6. Add data to the database.

## Using a MySQL Database

Switching to a MySQL database is similar to switching to a PostgreSQL database. The following steps will guide you through the process.

1. [Download and install MySQL](https://www.mysql.com/downloads/) from the official website. 

2. Install the Python adapter for MySQL:

```
pip install mysqlclient
```

3. Create a database in MySQL if you haven't done so.

4. Change your database settings in `settings.py`:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # Set to the appropriate host if you don't have MySQL on your local machine
        'PORT': '', # Leave it empty to use the default port (3306)
    }
}

5. Migrate your models to create the tables in PostgreSQL:

```
python manage.py migrate
```

6. Add data to the database.