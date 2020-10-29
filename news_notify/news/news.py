import re
from time import sleep
from datetime import datetime

from .client import Client
from .config import Config
from .utils import Utils
from ..db.engine import SQLiteEngine


class NotifyNews:
    notify_token: str = None
    last_notice_time: datetime = None

    def __init__(self, db_path: str, notify_token: str, proxies: dict = None) -> None:
        self.notify_token = notify_token
        self.engine = SQLiteEngine(db_path)
        self.client = Client(proxies)

    def refresh(self) -> None:
        res = self.client.get_request(
            Config.HOST + Config.PATH_LANG_JA + Config.PATH_NEWS
        )
        res.encoding = res.apparent_encoding

        for article_element in reversed(
            Utils.get_divs_by_class(res.text, "news-article")
        ):
            element = article_element.find_all(href=re.compile("news/"))[0]
            article = {
                "link": Config.HOST + element.get("href"),
                "title": element.text.strip(),
            }
            if self.engine.insert_article(article):
                if self.last_notice_time:
                    diff_sec = (datetime.now() - self.last_notice_time).total_seconds()
                    if diff_sec < Config.NOTIFY_SPAN:
                        sleep(Config.NOTIFY_SPAN)
                self.notify_message(article)

    def notify_message(self, article: dict):
        params = {
            "message": "\nNew article !!\n\n{title}\n{link}".format(
                title=article["title"], link=article["link"]
            )
        }
        headers = Config.NOTIFY_HEADERS.copy()
        headers["Authorization"] += self.notify_token
        self.client.post_request(Config.NOTIFY_URI, headers=headers, data=params)
        self.last_notice_time = datetime.now()
