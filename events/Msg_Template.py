from line_bot_api import *


def stock_reply_other(stockNumber):
    content_text = "及時股價和K線圖"

    text_message = TextSendMessage(
        text=content_text, 
        quick_reply=QuickReply(
        items=[
            QuickReplyButton(
                action=MessageAction(label="請輸入'#' + '股票代號'", text="#"+stockNumber)
            ), 
            QuickReplyButton(
                action=MessageAction(label="K線圖", text="@K"+stockNumber)
            )
        ]
        )
    )
    return text_message


def show_Button():
    flex_message = FlexSendMessage(
        alt_text="幣別種類",
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "幣別種類",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#AA2B1D",
                        "align": "center"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "美金",
                                    "text": "USD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#33daff",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "日圓",
                                    "text": "JPY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#33daff",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "英鎊",
                                    "text": "GBP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#4133ff",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "澳幣",
                                    "text": "AUD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#4133ff",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "加拿大幣",
                                    "text": "CAD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#9c33ff",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "港幣",
                                    "text": "HKD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#9c33ff",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "新加坡",
                                    "text": "SGD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#dd33ff",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "南非幣",
                                    "text": "ZAR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#dd33ff",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "菲比索",
                                    "text": "PHP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#ff339c",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "泰幣",
                                    "text": "THB"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#ff339c",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "越南盾",
                                    "text": "VND"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#ff3333",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "人民幣",
                                    "text": "CNY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#ff3333",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "韓元",
                                    "text": "KRW"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#ffc233",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "馬來幣",
                                    "text": "MYR"
                                },
                                "style": "primary",
                                "color": "#ffc233",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "印尼幣",
                                    "text": "IDR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#5cff33",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "紐元",
                                    "text": "NZD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#5cff33",
                                "margin": "sm"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "瑞典幣",
                                    "text": "SEK"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#33ffcf",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "瑞士法郎",
                                    "text": "CHF"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#33ffcf",
                                "margin": "sm"
                            }
                        ]
                    }
                ]
            }
        }

    )
    return flex_message
