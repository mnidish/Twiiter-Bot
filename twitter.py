import tweepy
import time

print("This is my twitter bot", flush = True)

CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET CODE'
ACCESS_KEY = 'YOUR ACCESS KEY CODE'
ACCESS_SECRET = 'YOUR ACCESS SECRET CODE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open (file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush = True)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)


    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush = True) 
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if 'hi' in mention.full_text.lower():
            print("Found hi!", flush=True)
            print("Responding back...", flush=True)
            api.update_status("hi " + '@' + mention.user.screen_name + " whats up!", mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
