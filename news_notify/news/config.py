class Config:
    HOST = "https://developers.line.biz"
    PATH_LANG_JA = "/ja"
    PATH_NEWS = "/news"

    NOTIFY_URI = "https://notify-api.line.me/api/notify"
    NOTIFY_SPAN = 0

    HEADERS = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36"
    }

    NOTIFY_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer ",
    }
