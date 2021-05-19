import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from src.response_handler import ResponseHandler, UnknownMessageError


# getting channel access token and secret token from environment variable
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

# initialize app & line api & handler
app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
response_handler = ResponseHandler('src/response.json')


# listening to Post Request from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# handling messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # get message from user
    received_message = event.message.text

    # find the corresponding response acording to the received message
    # if an unknown message is received, tell user that "I can't recognize it."
    try:
        responses = response_handler.response_to_message(received_message)
    except UnknownMessageError:
        responses = response_handler.unknown_message(received_message)
    # reply to user
    line_bot_api.reply_message(event.reply_token, responses)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)