import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uat_swim',
        'USER': 'bk',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': '10.138.60.129',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': "SET default_storage_engine=INNODB;",
        },
    }
}
