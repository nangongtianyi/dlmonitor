import os, sys
from os import path
import inspect
from dotenv import load_dotenv


PROJECT_ROOT = os.environ.get(
    'PROJECT_ROOT',
    path.dirname(path.dirname(inspect.getfile(inspect.currentframe()))))

load_dotenv(path.join(PROJECT_ROOT, '.env'))

DATABASE_ADDR = os.environ.get('DATABASE_ADDR', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'dlmonitor')
DATABASE_USER = os.environ.get('DATABASE_USER', "user")
DATABASE_PASSWD = os.environ.get('DATABASE_PASSWD', "pass")

DATABASE_URL = os.environ.get('DATABASE_URL', "postgresql://{}:{}@{}/{}".format(
    DATABASE_USER, DATABASE_PASSWD, DATABASE_ADDR, DATABASE_NAME))

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', "")
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', "")
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', "")
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET', "")

PDF_PATH = os.environ.get("PDF_PATH", "/tmp")
SOURCE_PATH = os.environ.get("SOURCE_PATH", "/tmp")
HOME_URL = os.environ.get("HOME_URL", "https://deeplearn.org")


MENDELEY_CLIENTID = os.environ.get("MENDELEY_CLIENTID", "")
MENDELEY_SECRET = os.environ.get("MENDELEY_SECRET", "")

SESSION_KEY = os.environ.get("SESSION_KEY", "DEEPLEARN.ORG SECRET KEY")
