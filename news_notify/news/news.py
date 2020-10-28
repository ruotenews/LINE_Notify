import re

from .client import Client
from .config import Config
from .utils import Utils
from ..db.engine import SQLiteEngine


class NotifyNews:
    def __init__(self, db_path: str) -> None:
        self.engine = SQLiteEngine(db_path)
        self.client = Client()

    def refresh(self) -> None:
        res = self.client.get_request(
            Config.HOST + Config.PATH_LANG_JA + Config.PATH_NEWS
        )
        res.encoding = res.apparent_encoding

        for article in Utils.get_divs_by_class(res.text, "news-article"):
            element = article.find_all(href=re.compile("news/"))[0]
            information = {
                "link": Config.HOST + element.get("href"),
                "title": element.text.strip(),
            }
            self.engine.insert_article(information)
