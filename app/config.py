import os
from dotenv import load_dotenv
import logging

load_dotenv()

class Config:
    FLASK_PORT = os.getenv('FLASK_PORT')
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'http://175.194.96.88')
    ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9222')
    ELASTICSEARCH_URL = f"{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"
    
    logger = logging.getLogger(__name__)
    logger.info(f"Config Elasticsearch URL: {ELASTICSEARCH_URL}")
