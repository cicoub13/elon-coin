import tweepy
import telegram
import credentials

# Twitter API Auth
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Telegram Bot Auth
bot = telegram.Bot(token=credentials.BOT_TOKEN)

# Function to test if tweet is "interesting"
def is_tweet_interesting(tweet_text):
    return "crypto" in tweet_text or "$" in tweet_text

# Fetch last 100 tweets
tweets = api.user_timeline(screen_name='elonmusk',
                           count=100,
                           include_rts = False,
                           tweet_mode = 'extended')

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
            bot.send_message(chat_id = credentials.MY_CHAT_ID, text = "Elon Musk a tweeté : " + tweet.full_text)
            print("ID: {} notified".format(tweet.id))
            # Store Tweet ID in file to notify only once
            f.write(str(tweet.id) + '\n')

f.close()
        