from typing import Any, Optional
import requests
from config.config import Config

class ApiClient:
    def __init__(self, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.base_url = (base_url or Config.BASE_URL).rstrip("/")
        self.timeout = timeout or Config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path: str, params: Optional[dict[str, Any]] = None) -> requests.Response:
        return self.session.get(f"{self.base_url}{path}", params=params, timeout=self.timeout)

    def post(self, path: str, json: Optional[dict[str, Any]] = None) -> requests.Response:
        return self.session.post(f"{self.base_url}{path}", json=json, timeout=self.timeout)

    def delete(self, path: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}{path}", timeout=self.timeout)
