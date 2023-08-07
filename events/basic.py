from line_bot_api import *


def about_us_event(event):
    emoji = [
        {
            "index":0,
            "porductId": "6359",
            "emojiId": "11069851",
        },
        {
            "index": 17,
            "porductId": "5ac2213e040ab15980c9b447",
            "emojiId": "006",
        },
    ]
    test_message = TextSendMessage(text='''$ Master Finance $
    Hello! 歡迎加入財經小幫手''',emoji=emoji)
    sticker_message = StickerSendMessage(
        package_id="8522",
        sticker_id="16581271",
        )
    line_bot_api.reply_message(
        event.reply_token,
        [test_message,sticker_message])
def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))
def Usage(event):
    push_msg(event,"  🤞🤞查詢方法🤞🤞  \
                   \n\
                   \n 🎺小幫手可以查詢油價、股票、匯率\
                   \n 🎈油價通知→→→輸入查詢油價\
                   \n 🤗匯率通知→→→輸入查詢匯率\
                   \n 🙄匯率兌換→→→換匯USD/TWD\
                   \n 😁股價查詢→→→輸入#股票代碼")
def popbar(event):
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