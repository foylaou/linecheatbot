from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# Channel access token
line_bot_api = LineBotApi("jvP6prUhvT+cbHtN3B/cEgugl32WUAA1Oy1CD7FJE/vmcdv8wRgWAd+0lfi83dJEsEv6/2R8cDyJad5BF5F9Icrp++c9bzNjGzoxppc2kf6bJYio6Hk0r/zs1sVD4LW9C2v6lQC834wnP0I888kX6QdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("974df81e00a95ccd63aab56e02f62d52")