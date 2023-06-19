import requests
from telegram import (Update)
from telegram.ext import CallbackContext


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

    
