from dotenv import load_dotenv, find_dotenv
from os import getenv as env
from uuid import uuid4

#App
load_dotenv(find_dotenv())

SECRET_KEY = f"{uuid4().hex}-{uuid4().hex}"
DEBUG = int(env('DEBUG', '1'))

#MySQL
MYSQL_HOST = env('MYSQL_HOST', 'localhost')
MYSQL_PORT = env('MYSQL_PORT', 3306)
MYSQL_USER = env('MYSQL_USER', 'root')
MYSQL_PASSWORD = env('MYSQL_PASSWORD', '')
MYSQL_DB = env('MYSQL_DB', 'test')

#Server
PORT = int(env('PORT', 5000))
HOST = env('HOST', 'localhost')