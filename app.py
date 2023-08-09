from line_bot_api import *
from events.basic import *
from events.oil import *
from events.msg_Template import *
app = Flask(__name__)


@handler.add(MessageEvent, message=TextMessage)
def handl_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    emsg = event.message.text

    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)
    if message_text == '想知道油價':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
        #股票區

    if message_text == '股價查詢':
        line_bot_api.push_message(
            uid,
            TextSendMessage("請輸入'#' + '股票代號'\n範例：#2330")
        )
    if message_text == '@小幫手':
        popbar(event)

    if re.match("想知道股價[0-9]:", msg):
        stockNumber = msg[2:6]
        btn_msg = stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0

    if (emsg.startswith('#')):
        text = emsg[1:]
        content = ''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp'] + 8 * 60 * 60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content += '%s (%s) %s\n' % (
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)

        content += '現價: %s / 開盤: %s\n' % (
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content += '最高: %s / 最低:%s\n' % (
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])

        content += '量: %s\n' % (stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
        if re.match("想知道股價[0-9]:", msg):
            stockNumber = msg[2:6]
            btn_msg = stock_reply_other(stockNumber)
            line_bot_api.push_message(uid, btn_msg)
            return 0

    if (emsg.startswith('#')):
        text = emsg[1:]
        content =''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content +='%s (%s) %s\n' % (
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)

        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content += '最高: %s / 最低:%s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])

        content += '量: %s\n'%(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
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
    # app.run(host="0.0.0.0", ssl_context=('server.crt', 'server.key'))
