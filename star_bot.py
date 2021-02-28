
#imports libraries
from decouple import config
import requests
from telegram.ext import Updater, MessageHandler, Filters

token = config('TOKEN') #gets telegram token
request_url = config('REQUEST_URL') #gets request url from github API

updater = Updater(token=token)
dispatcher = updater.dispatcher #delivers updates to dispatcher


def handler(bot, update):
    api = requests.get(url=request_url)
    response = api.json() #gets the json response from the API
    request = update.message.text
    result = ""
    for data in response:
        if data['name'] != request:
            continue
        result = "Repository '%s' has %d Stars." % (request, data['stargazers_count']) #shows the stars of the repositories
        break
    if result == "": #if the repository is not found, prints an error message
        result = "Repository not found."
    update.message.reply_text(result)


dispatcher.add_handler(MessageHandler(Filters.text, handler))

updater.start_polling()
updater.idle()
