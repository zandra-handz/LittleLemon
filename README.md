# Littlelemon API (Backend Capstone for Meta)

## Description

Hello fellow classmates! :) Here is my project for the backend capstone course.

### Setup

You will want to establish a virtual environment and activate at the littlelemon/ level before running and testing.

Cd to littlelemonroot/ project folder to run the server and to run the tests. See the readme.txt for endpoints!

### Database Configuration

**This project uses a MySQL database.**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Littlelemon',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### Author

[@zandra-handz](https://github.com/zandra-handz)

