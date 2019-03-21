from .common import *

# DATABASE_URL = 'postgres://ngaqewugzbioaw:496f58b862e9d2e510dcc70ed40fb558ca95cac9d79696c248fdb86bc3274c4f@ec2-54-221-201-212.compute-1.amazonaws.com:5432/daamav0pvf79ht'
DATABASE_URL = 'postgres://postgres:secret@localhost:5432/postgres'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
