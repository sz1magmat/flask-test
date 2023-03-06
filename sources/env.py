"""Loading environment variables from .env file"""

from os import getenv
from create import log

def get_env(key):
    env = getenv(key)
    if env: return env
    else: log.error("Env variable not found"); exit(f"Env variable not found - {key}")