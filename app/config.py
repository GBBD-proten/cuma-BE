from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_PORT = environ.get('FLASK_PORT')
    ELASTICSEARCH_URL = environ.get('ELASTICSEARCH_HOST') + ':' + environ.get('ELASTICSEARCH_PORT')