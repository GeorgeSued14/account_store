from dotenv import load_dotenv
from pathlib import Path

import os 

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG")
JSON_SORT_KEYS = os.getenv("JSON_SORT_KEYS")


