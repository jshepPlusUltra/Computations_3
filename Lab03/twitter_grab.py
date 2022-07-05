import tweepy
import sys
import random

# Go to http://apps.twitter.com and create an app.
# Authentication keys/tokens (STS dev)
consumer_key = 'HU5D0SosXuzWisbWjD3XhxWPu'
consumer_secret = '3lm4ujYqWc82yx25biI6HhEO4Z6nfrDgZDsqLl8BigRwOlLjFc'

token = '1381657141044334596-NAbihelvjOIkXZPQs1HfkxbSeWO4oZ'
token_secret = '9fbdTYO5GzO18IM0JsLwoIDt1OtpWURh1PTBO8Xxasr4S'


if __name__ == '__main__':
    # Authorization variable
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret) 

    #tweet_hash_key = str(sys.argv[0])

    # Packaged API call information
    api = tweepy.API(auth, wait_on_rate_limit=True)


    count = 0
    i = 0
    tweeter_list = []
    # Using the Cursor object (great documentation available)
    while i < 3:
        tweeter_sub_list = [] # The list is being reset every time. 
        for tweet in tweepy.Cursor(api.search,
                               q = "My Hero Academia",
                               lang = "en",
                               results = 'current',
                               count = 100).items(1000): # If i left items() blank, I would get all of tweets
#         print(len(tweeter_sub_list))
#         print(tweet.created_at, tweet.text)
            tweeter_sub_list.append((tweet.created_at, tweet.text))
            if len(tweeter_sub_list) == 300:
                #print(len(tweeter_sub_list))
                theSample = random.sample(tweeter_sub_list, 100) # pulling a random sample out of the 100
                tweeter_sub_list.append(theSample)
            count += 1
        #print(tweeter_sub_list)
        tweeter_list.append(tweeter_sub_list) # After we go through the first 300 then append to a new list
        i += 1
    #print(tweeter_list)

    # Printting the tweets so I can push through to a text file for further processing. 
    for main_list in tweeter_list: # Length 3
        for date_time,tweet in main_list: 
         print(date_time)
         print(tweet)
