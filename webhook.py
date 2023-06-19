from telegram import Bot
from bot import TOKEN

bot  = Bot(TOKEN)

def set_webhook(url):
    print(bot.set_webhook(url=url))
set_webhook("https://stanger.pythonanywhere.com/webhook/")