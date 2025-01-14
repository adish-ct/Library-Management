import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Get the logger for this module
logger = logging.getLogger('myapp')

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

USE_POSTGRES = os.getenv('USE_POSTGRES', False)


if USE_POSTGRES:
    try:
        logger.info("Connecting to postgres")
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'library_management'),
            'USER': os.getenv('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
        }
    }
    except Exception as e:
        logger.error(f"Error connecting to PostgreSQL database {str(e)}")
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    logger.info("Using SQLite database")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }