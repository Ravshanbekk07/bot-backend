from flask import Flask, request
import requests

from call_back_fu import secstart

bot_app = Flask(__name__)


TOKEN = '6083785294:AAHy_BRexQquv_DEcNRwdSbqCS-AdPHd4Ks'


@bot_app.route('/webhook/', methods=['POST', 'GET'])
def webhook_bot():
    if request.method == 'GET':
        return 'webhook is running'
    elif request.method == 'POST':
        update = request.get_json()

        chat_id = update['message']['chat']['id']
        first_name = update['message']['chat']['first_name']
        text = update['message']['text']
        if text == '/start':
            secstart(chat_id, first_name)

        else:
            payload = {
                'chat_id': chat_id,
                'text': text
            }
        requests.get(
            f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=payload)
    return 'cool'
