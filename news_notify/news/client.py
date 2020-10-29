from requests import Session, Response
from requests.exceptions import ConnectTimeout, ReadTimeout

from .config import Config
from .exception import ReadTimeoutError, ConnectionTimeoutError


class Client:

    proxies: dict = None
    session: Session = None

    def __init__(self, proxies: dict = None) -> None:
        self.proxies = proxies
        self.init_connection()

    def init_connection(self) -> None:
        self.session = Session()

    def get_request(
        self, url: str, headers: dict = None, params: dict = None
    ) -> Response:
        try:
            if headers is None:
                headers = Config.HEADERS
            return self.session.get(
                url=url,
                headers=headers,
                params=params,
                proxies=self.proxies,
                timeout=5.0,
            )
        except ConnectTimeout:
            raise ConnectionTimeoutError("[get failed] connection timeout.")
        except ReadTimeout:
            raise ReadTimeoutError("[get failed] read timeout.")
        except Exception:
            raise

    def post_request(
        self,
        url: str,
        headers: dict = None,
        json: dict = None,
        data: dict = None,
    ) -> Response:
        try:
            if headers is None:
                headers = Config.HEADERS
            return self.session.post(
                url=url,
                headers=headers,
                json=json,
                data=data,
                proxies=self.proxies,
                timeout=5.0,
            )
        except ConnectTimeout:
            raise ConnectionTimeoutError("[post failed] connection timeout.")
        except ReadTimeout:
            raise ReadTimeoutError("[post failed] read timeout.")
        except Exception:
            raise
