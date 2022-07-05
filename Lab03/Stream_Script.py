from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = 'HU5D0SosXuzWisbWjD3XhxWPu'
consumer_secret = '3lm4ujYqWc82yx25biI6HhEO4Z6nfrDgZDsqLl8BigRwOlLjFc'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
#access_token= '<Your Token Here>'
#access_token_secret= '<Your Secret Token Here>'
access_token = '1381657141044334596-NAbihelvjOIkXZPQs1HfkxbSeWO4oZ'
access_token_secret = '9fbdTYO5GzO18IM0JsLwoIDt1OtpWURh1PTBO8Xxasr4S'



class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    #stream.sample()                        # This grabs a random sample of tweets
    stream.filter(track=['One Piece'], languages=['en'])
