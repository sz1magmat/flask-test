"""Loading environment variables from .env file"""

from os import getenv
from create import log

try: from dotenv import load_dotenv
except ImportError as e: log.error("Import error - %s", e); raise

def get_env(key):
    try: load_dotenv()
    except FileNotFoundError: log.error("Env file not found"); raise

    env = getenv(key)
    if env: return env
    else: log.error("Env variable not found"); exit(f"Env variable not found - {key}")
