from flask import Flask, request
import requests

from call_back_fu import secstart

bot_app = Flask(__name__)


TOKEN = '6083785294:AAHy_BRexQquv_DEcNRwdSbqCS-AdPHd4Ks'

def send_m(chat_id):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    update = request.get_json()
    text = update['message']['text']
    number = 0
    disnum = 0
    while True:
        if text =='like👍':
            number+=1
              
        elif text == 'dislike👎':
            disnum+=1  

    payload = {
        "chat_id":chat_id,
        'text':f'like {number}\n dislike { disnum}',
        
        
    }
    response = requests.post(URL,json=payload)
    return response
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
        elif text =='like👍':
            send_m(chat_id)
        elif text == 'dislike👎':
            send_m(chat_id)
        else:
            payload = {
                'chat_id': chat_id,
                'text': text
            }
            requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=payload)
    return 'cool'
