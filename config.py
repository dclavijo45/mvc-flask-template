from dotenv import load_dotenv, find_dotenv
from os import getenv as env
load_dotenv(find_dotenv())
import random
import string

#App
SECRET_KEY = ''.join(random.
    choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") 
    for i in range(20))

DEBUG = int(env('DEBUG', '1'))

#Server
PORT = int(env('PORT', 5000))
HOST = env('HOST', 'localhost')