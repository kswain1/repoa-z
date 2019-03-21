from .settings import *


DATABASE_URL = 'postgres://hjandlpzmpienu:0c3e550f0a4bcf6d1749a7709d8e5da778362fc4727cd07c5710f1d3cdf289ae@ec2' \
               '-54-227-244-12.compute-1.amazonaws.com:5432/d80gibomf6hbh2'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
