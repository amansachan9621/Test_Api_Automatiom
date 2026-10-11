import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))
