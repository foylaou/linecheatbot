from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)


@handler.add(MessageEvent, message=TextMessage)
def handl_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    message_text = str(event.message.text).lower()

    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)
    if message_text == '想知道油價':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
    if message_text == '股價查詢':
        line_bot_api.push_message(
            uid,
            TextSendMessage("請輸入'#' + '股票代號'\n範例：#2330")
        )
    if message_text == '@小幫手':
        popbar(event)
@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = '''Hello! 歡迎加入財經小幫手'''
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg)
    )

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(100)

    return 'OK'




if __name__ == "__main__":
    app.run()
