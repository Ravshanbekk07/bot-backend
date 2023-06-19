import requests
from telegram import (Update)
from telegram.ext import CallbackContext

TOKEN='6083785294:AAHy_BRexQquv_DEcNRwdSbqCS-AdPHd4Ks'

def start(update: Update, context: CallbackContext) -> None:
  
    first_name = update.message.chat.first_name
    last_name=update.message.chat.last_name
    username=update.message.chat.username
    doc_id=update.message.chat_id


    url = 'http://rramazonov.pythonanywhere.com/users/'
    
    response = requests.post(url,json={"first_name": first_name, "last_name": last_name, "username": username,"chat_id":doc_id})
    if response.status_code ==200:
        update.message.reply_html(text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz ")
    else:
        update.message.reply_html(text=f"Hello again , <b>{first_name}</b>. siz allaqachon royxatdan otgansiz")


def secstart(chat_id,first_name):
    # updates = response.json()['result']
    # last_update = updates[-1]

    # chatid = last_update['message']['chat']['id']
    # firstname = last_update['message']['chat']['first_name']
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    btn1 = 'like 👍'
    btn2 = 'dislike 👎'
    keyboard = [[btn1,btn2]]
    payload = {
        "chat_id":chat_id,
        'text':f'{first_name } ovozingiz biz uchun muhim',
        
        'reply_markup': {
        'keyboard': keyboard,
        'resize_keyboard':True
        }
    }
    response = requests.post(URL,json=payload)
    return response
   




