import tweepy
import time
import random
from datetime import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler("u6pTX2Z7zA8wGJwpqb8KGjsow", "whgBqzOxiCMxJtHXeooEHZtFMvdhzcG8Jj0TiQjixV20ucDtMU")
auth.set_access_token("1379804667471933442-qVm0G3ZIf7BYMjiqaDWO8gU8rT2pvm",
                      "yUCXJdsyaLJ68KxJ20VM6rrp5lP7bW1t1h2WNxMJ6Q3gR")

# Create API object
api = tweepy.API(auth)

count = 0

count_shits = 0
count_message = 0
count_error = 0
# api.update_status("@lordyiming welcome to my experiment.")

while True:

    current_hour = datetime.utcnow().hour
    time_frame = ""

    if 6 <= current_hour < 12:
        time_frame = "Good Morning"
    elif 12 <= current_hour < 16:
        time_frame = "Good Afternoon"
    elif 16 <= current_hour < 20:
        time_frame = "Good Evening"
    else:
        time_frame = "Good Night"

    rand_text = ["I hope you're a better man today.", "how are you doing today?", "This is fun ahahah.",
                 "I took %d shits since the beginning." % count_shits, "I have %d shits to clean" % count_shits,
                 "I feel %d kg lighter since the beginning of this project." % count_shits, "uhhh?",
                 "HAHAHAHAHAHAHA", "what a time to be a robot.", "why am I wasting time on this",
                 "if you don't reply to this tweet, i'll keep posting more, jk it's never going to end."
                 "I AM A REAL PERSON", "I hope you enjoy this experiment.",
                 "You have received %s tweets from me since the beginning." % count, "lol.",
                 "ha.ha.ha.ha.ha.ha.ha.ha.ha.ha.ha.ha.", "I think this might be enough variety,",
                 "OY! OY! this message was signed by the pirate gang", "you are now more intelligent.",
                 "you are now more stupid.", "I have also a fat ass too, it's %d kg." % (count_message + count_shits),
                 "please have a great time.", "you have to enjoy this tweet.",
                 "this tweet is intended to be hilarious please laugh.", "this is very funny!", "this is not funny.",
                 "it is %s." % datetime.utcnow().strftime("%H:%M:%S"), "a new notification.",
                 "this is coded in Python but I prefer Java.", "I am a real human being!", "not %s" % time_frame,
                 "I think you had enough of that shit.", "enjoy this tweet this is an order.",
                 "I hope you find those tweet creative, or not, I don't care, I do care, uhg.", "YES!", "NO!",
                 "Hello World, Mr Robert is not a camel.", "1.", "2.", "3.", "4.", "1,2,3 and 4.", "or is it?",
                 "am I muted yet?", "UwU ヾ(•ω•`)o.", "wow!", "uh, something's not right.", "certified originalTM.",
                 "we havin' good craid ain't we.", "I am not a bot, you are a bot.", "No?", "Mutton", "Jdiwkwnwlsp",
                 "if you're seeing this I'm dead, or not", "Im getting heavier! My arse is %s kg!" % count, "yoyoy",
                 "je parle aussi francais mdr."]

    rand_adj = ["beautiful", "attractive", "pretty", "handsome", "good-looking", "nice-looking", "pleasing", "alluring",
                "prepossessing", "as pretty as a picture", "lovely", "charming", "delightful", "appealing", "smelly",
                "foul-smelling", "evil-smelling", "stinking", "stinking to high heaven", "reeking", "fetid",
                "malodorous", "pungent", "acrid", "rank", "putrid", "noxious", "gamy", "gorgeous", "king"]

    try:
        api.update_status("%s %s @lordyiming, %s" % (time_frame, random.choice(rand_adj), random.choice(rand_text)))
    except tweepy.TweepError as e:
        if e.api_code == 187:
            count_error += 1
            api.update_status("%s %s @lordyiming, %s originality: - %d " % (time_frame, random.choice(rand_adj),
                                                                            random.choice(rand_text), count_error))
        else:
            pass

    sleeping_time = random.randint(30, 240)

    count_shits += 1
    count += 1

    print("Amount of shit posted : %d" % count)
    print("Sleeping time: %d s\n-----------------------" % sleeping_time)
    time.sleep(sleeping_time)

# api.update_status("@lordyiming")
