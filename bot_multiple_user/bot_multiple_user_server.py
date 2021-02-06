import tweepy
import telegram
import credentials
from telegram.ext import Updater
from telegram.ext import CommandHandler
import sched, time

# Twitter API Auth
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Telegram Bot Auth
bot = telegram.Bot(token=credentials.BOT_TOKEN)
updater = Updater(token=credentials.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    f = open("chat_ids", "a")
    update.message.reply_text("Bienvenue. Vous seriez notifié(e) à chaque fois qu'Elon Musk tweet à propos de crypto-monnaie.")
    f.write(str(update.effective_chat.id) + '\n')
    f.close()
    print("User {} added".format(str(update.effective_chat.id)))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

# Function to test if tweet is "interesting"
def is_tweet_interesting(tweet_text):
    return "crypto" in tweet_text or "$" in tweet_text

def send_telegram_message_to_all_users(text_message):
    f = open("chat_ids", "r")
    chat_ids = f.read().splitlines()
    for chat_id in chat_ids:
        bot.send_message(chat_id = chat_id, text = text_message)
    f.close()

def read_tweets(sc):
    # Fetch last 100 tweets
    tweets = api.user_timeline(screen_name='elonmusk',
                            count=100,
                            include_rts = False,
                            tweet_mode = 'extended')
    print("Read tweets")

    # Read already notified tweets
    f = open("tweet_ids", "r")
    tweets_already_notified = f.read().splitlines()
    f.close()

    f = open("tweet_ids", "a")
    for tweet in tweets:
        # If tweet already notified
        if str(tweet.id) not in tweets_already_notified:
            if is_tweet_interesting(tweet.full_text):
                # Notify Telegram user
                send_telegram_message_to_all_users("Elon Musk a tweeté : " + tweet.full_text)
                print("ID: {} notified".format(tweet.id))
                # Store Tweet ID in file to notify only once
                f.write(str(tweet.id) + '\n')

    f.close()
    s.enter(60, 1, read_tweets, (sc,))
            
# Cron
s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, read_tweets, (s,))
s.run()