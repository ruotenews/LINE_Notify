from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base, News


class SQLiteEngine:
    def __init__(self, db_path: str) -> None:
        engine = create_engine(f"sqlite:///{db_path}", echo=True)
        Base.metadata.create_all(bind=engine)
        self.session = Session(bind=engine)

    def insert_article(self, article: dict) -> bool:
        news = News()
        news.link = article["link"]
        news.title = article["title"]
        self.session.add(news)
        self.session.commit()
