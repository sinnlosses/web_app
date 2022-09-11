# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#     }
# }
SECRET_KEY = 'XXXXXXX'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'password',
        'HOST': 'db_hostname_or_ip',
        'PORT': 'db_port',
    }
}