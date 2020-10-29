import os
from dotenv import load_dotenv

from news_notify.news import NotifyNews

load_dotenv(verbose=True)
load_dotenv('.env')

DB_FILE_PATH = os.environ.get("DB_FILE_PATH")
NOTIFY_TOKEN = os.environ.get("NOTIFY_TOKEN")

notify_news = NotifyNews(DB_FILE_PATH, NOTIFY_TOKEN)
notify_news.refresh()
