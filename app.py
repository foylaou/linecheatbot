from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)


@handler.add(MessageEvent, message=TextMessage)
def handl_message(event):
    profile = line_bot_api.get_profile(event.score.user_id)
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '@小幫手':
        buttons_template = TemplateSendMessage(
            alt_text='小幫手 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/UWHsztk.png',
                actions=[
                    MessageTemplateAction(
                        label='油價查詢',
                        text='想知道油價'
                    ),
                    MessageTemplateAction(
                        label='匯率查詢',
                        text='匯率查詢'
                    ),
                    MessageTemplateAction(
                        label='股價查詢',
                        text='股價查詢'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

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


if __name__ == "__main__":
    app.run()
