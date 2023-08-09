from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# Channel access token
line_bot_api = LineBotApi("JI8HVi4hH1wgm/MSbtzvkVPzNTwdm/n7xYNarm6ihncmZYE4bIWQltX4vkkbhddQ53WYjPogi2t3HJZ0sP7HWwzTj8hXnlGdAQCQKakd17V8aJsdOsnbLsdfnYbsocHV7RZgWGxMEErhvsJINSwOQAdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("9c9988921e51c8665c58a28070278628")