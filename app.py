# LineBot所需套件
from line_bot_api import *
from events.basic import *

app = Flask(__name__)


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
@handler.add(MessageEvent, message=TextMessage)
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    app.logger.info("Request body: "+body)
    try:
        handler.handel(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
def handle_message(event):
    emoji = [
        {
            "index":0,
            "productId": "5ac2213e040ab15980c9b447",
            "emojiId": "002",
        },
        {
            "index": 17,
            "productId": "5ac2213e040ab15980c9b447",
            "emojiId": "002",
        },
    ]
    test_message = TextSendMessage(text='''$ Master Finance $ Hello! 你好，你住哪裡?我住高雄，約嗎?''',emoji=emoji)
    sticker_message = StickerSendMessage(
        package_id="8522",
        sticker_id="16581271",
        )
    line_bot_api.reply_message(
        event.reply_token,
        [test_message,sticker_message])
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
