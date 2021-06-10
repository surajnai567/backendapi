import hashlib
import logging
import os
from typing import Optional
from exceptions import MissingEnvVarError

def make_password(password):
    assert password
    hash = hashlib.md5(password).hexdigest()
    return hash

def check_password(hash, password):
    """Generates the hash for a password and compares it."""
    generated_hash = make_password(password)
    return hash == generated_hash

def get_env_var(env_var_name: str, required=True) -> Optional[str]:
    """Gets the environment variable of the specified name"""
    try:
        return os.environ[env_var_name]
    except KeyError:
        if required:
            raise MissingEnvVarError
        else:
            logging.debug(f'Optional env var {env_var_name} is not set')
            return None

print(type(make_password('hi'.encode())))