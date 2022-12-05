import os
from dotenv import load_dotenv


# Load .env variables as environment variables
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# SLACK
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')
SLACK_ICON = os.environ.get('SLACK_ICON')
SLACK_USERNAME = os.environ.get('SLACK_USERNAME')
