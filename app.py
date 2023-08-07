# LineBot所需套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# Channel access token
line_bot_api = LineBotApi("jvP6prUhvT+cbHtN3B/cEgugl32WUAA1Oy1CD7FJE/vmcdv8wRgWAd+0lfi83dJEsEv6/2R8cDyJad5BF5F9Icrp++c9bzNjGzoxppc2kf6bJYio6Hk0r/zs1sVD4LW9C2v6lQC834wnP0I888kX6QdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("974df81e00a95ccd63aab56e02f62d52")


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


# 處理訊息
@handler.add(MassageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
