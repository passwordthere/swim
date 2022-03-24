import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'swim',
        'USER': 'focusonme',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'focusonme.mysql.pythonanywhere-services.com',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': "SET default_storage_engine=INNODB;",
        },
    }
}
