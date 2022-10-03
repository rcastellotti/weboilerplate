import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
    SITE = os.getenv("SITE")
