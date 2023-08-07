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


if __name__ == "__main__":
    app.run()
