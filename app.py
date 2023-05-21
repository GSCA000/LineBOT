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

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


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
    
