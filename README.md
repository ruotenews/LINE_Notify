# notify-line-dev-news
[LINE Developer news](https://developers.line.biz/ja/news/) が更新された時にLINE Notifyで通知するスクリプト

cron設定すると最新情報を素早くLINEで通知できる。

## Setup
```bash
$ pip install -r requirements.txt
$ cp .env.sample .env
```

## Step1
[こちら](https://notify-bot.line.me/my/)からLINEにログインして、通知したいトークルームを選び、トークン発行。

**Setup** で作成した`.env`の`NOTIFY_TOKEN`にトークンを記載。  
データベース名を変更したい時は`DB_FILE_PATH`を変更。

```bash
DB_FILE_PATH="news.sqlite"
NOTIFY_TOKEN="iEET2ScqVhKrt45ZTXXXXXXXXXXXX"
```

## Step2
実行する。
```bash
$ python3 notice.py
```

## 注意
初回実行はデータベースにデータが無いので、連続して沢山の通知が来る。  
そのため、`./news_notify/news/config.py`に`NOTIFY_SPAN`を設けてある。  
この値を書き換えると、指定した秒数ごとに通知を行うことができる。

```python
NOTIFY_SPAN = 0
```

## Lint
- black
- flake8
