# StarBot
StarBot is a sample bot for Telegram which makes use of the GitHub API to fetch data. This project was written as part of [Google Code-in](https://codein.withgoogle.com/).

### Usage
Message the bot with the name of a repository located under the user or organisation of the request URL. The bot will reply with the number of Stars held by that repository.

 - You can use [BotFather](https://telegram.me/BotFather) to generate a token for Telegram.
 - Place the token and GitHub request URL in a .env file. A sample is provided via `.env.sample`.
 
 ### Requisites:
 - Decouple python
```
pip install python-decouple
```
- Python Telegram Library (https://github.com/python-telegram-bot/python-telegram-bot) 
```
pip install python-telegram-bot --upgrade
```
