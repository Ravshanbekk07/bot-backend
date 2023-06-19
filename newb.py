from flask import Flask,request
import requests


bot_app = Flask(__name__)
TOKEN='6083785294:AAHy_BRexQquv_DEcNRwdSbqCS-AdPHd4Ks'

@bot_app.route('/webhook/',methods = ['POST','GET'])
def webhook_bot():
    if request.method =='GET':
        return 'webhook is running'
    elif request.method =='POST':
            update =request.get_json()
            print(update)
            chat_id = update['message']['chat']['id']
            text = update['message']['text']

            payload={
                 'chat_id':chat_id,
                 'text':text
            }
            requests.get(url=f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=payload)

            return 'cool'

