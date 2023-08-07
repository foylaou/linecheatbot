from line_bot_api import *


#
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
