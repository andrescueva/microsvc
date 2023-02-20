"""dependencies module
"""
import os
import jwt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


transaction_ids = []

def is_api_key_valid(x_parse_rest_api_key: str):
    """Validate api key """
    if x_parse_rest_api_key != API_KEY:
        return False
    return True


def create_jwt(transaction_id: int):
    """create jwt token"""
    transaction_ids.append(transaction_id)
    payload = {"transaction_id": transaction_id}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


def is_valid_token(token: str):
    """check is token is valid"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        transaction_id = payload["transaction_id"]
        if transaction_id in transaction_ids:
            return True
    except jwt.InvalidTokenError:
        return False


def invalidate_token(token: str):
    """remove transaction id from list of current ids"""
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    transaction_id = payload["transaction_id"]
    transaction_ids.remove(transaction_id)


class IdGenerator():
    """Generator id autoincremental"""
    def __iter__(self) -> None:
        self.count = 0
        return self

    def __next__(self):
        counter =  self.count
        self.count += 1
        return counter
