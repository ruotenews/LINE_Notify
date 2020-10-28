import os
from dotenv import load_dotenv

from news_notify.news import NotifyNews

load_dotenv(verbose=True)
load_dotenv('.env')

DB_FILE_PATH = os.environ.get("DB_FILE_PATH")

notify_news = NotifyNews(DB_FILE_PATH)
notify_news.refresh()
