from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class News(Base):

    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    link = Column(String(length=255))
    title = Column(String(length=255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
