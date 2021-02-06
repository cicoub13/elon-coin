# Telegram Bot to notify about Elon Musk tweets

## Context

You can read article here : https://www.fotozik.fr/developper-un-bot-en-python-qui-surveille-les-tweets-delon-musk in :fr:

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

Launch script in a detached session (like screen)

`*/5 * * * * python3 ~/workspace/elon-coin/bot_multiple_user/bot_multiple_user_server.py`