from line_bar_api import *

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

