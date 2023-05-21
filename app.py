from flask import Flask, request, abort

from linebot import(
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)

import json

app = Flask(__name__)

line_bot_api = LineBotApi("9z7WqVYeoYfJW/lV+OPX8I2XUzmk8XWkgp9jYMZacYgZ++a9f/P8wRUIDImCrd7pgFqbIkDatcfLT7od8EW00QqtXBnwcf6tLA8uohGRB3Oly0qVjiTai90Fy85f+lgxdNOPCWwJ/yt1QSoG7qlp9QdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("d0b0433b07bf679eff81a4984609fa0e")


def push():

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    json_str=json.dumps(json_data,indent=4)
    print(json_str)
    
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    json_data = json.loads(str(event))
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    
@app.route("/broadcast")

def broadcast_message():
    if request.args.get("message"):
        message = request.args.get("message")
        try:
            line_bot_api.broadcast(TextSendMessage(message))
            return "Broadcast OK"
        except:
            return "Broadcast FAILED"

if __name__ == "__main__":
    app.run(port=3838)
    
