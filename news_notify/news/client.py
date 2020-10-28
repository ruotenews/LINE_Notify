import requests
from requests.exceptions import ConnectTimeout, ReadTimeout

from .config import Config
from .exception import ReadTimeoutError, ConnectionTimeoutError


class Client:

    proxy: str = None
    session: requests.Session = None

    def __init__(self, proxy: str = None) -> None:
        self.proxy = proxy
        self.init_connection()

    def init_connection(self) -> None:
        self.session = requests.Session()

    def get_request(
        self, url: str, headers: dict = None, params: dict = None
    ) -> requests.Response:
        try:
            if headers is None:
                headers = Config.HEADERS
            return self.session.get(
                url=url,
                headers=headers,
                params=params,
                proxies=self.proxy,
                timeout=5.0,
            )
        except ConnectTimeout:
            raise ConnectionTimeoutError("[get failed] connection timeout.")
        except ReadTimeout:
            raise ReadTimeoutError("[get failed] read timeout.")
        except Exception:
            raise
