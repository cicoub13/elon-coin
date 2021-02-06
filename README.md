# Telegram Bot to notify about Elon Musk tweets

## Context

You can read article here : 

## Install

Clone repository:

```
git clone https://github.com/cicoub13/elon-coin.git
cd elon-coin
```

Create a `credentials.py`and fill it with needed data.

Install needed libraries :

`pip3 install tweepy python-telegram-bot`

## Bot mono user

Add a cron to execute file bot_one_user/bot_one_user.py every 5 minutes:

`*/5 * * * * python3 ~/workspace/elon-coin/bot_one_user/bot_one_user.py`

## Bot multi users

Start server to listen to /start commands and add users in a list to notify:

`python3 ~/workspace/elon-coin/bot_multiple_user/bot_multiple_user_server.py`

Add a cron to execute file bot_multiple_user/bot_multiple_user_cron.py every 5 minutes:

`*/5 * * * * python3 ~/workspace/elon-coin/bot_multiple_user/bot_multiple_user_cron.py`