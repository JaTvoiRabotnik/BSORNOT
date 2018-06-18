"""
Bot that analyses if a tweet is BS or not.

Will listen to mentions of @BSORNOT1 and reply with its
assessment of whether the text is BS.
"""
import tweepy
import secrets


# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)

auth.set_access_token(secrets.access_token, secrets.access_secret)

# Construct the API instance
api = tweepy.API(auth)  # create an API object

''' Things we can do with the REST API:
# get all public tweets:
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# get list of followers:
user = api.get_user('BOTORNOT1')
for friend in user.friends():
    print(friend.screen_name)
'''


def tweet_response(text, username, status_id):
    """Respond to query for a BS evaluation."""
    answer = " I don't know yet if this is BS or not."

    api.update_status(status='@{0}'.format(username) + answer,
                      in_reply_to_status_id=status_id)


# create a class inherithing from the tweepy StreamListener
class BotStreamer(tweepy.StreamListener):
    """
    Streamer class for using Twitter Streaming API.

    Called when a new status arrives which is passed down from the on_data
    method of the StreamListener
    """

    def on_status(self, status):
        """Event called when a new status arrives."""
        username = status.user.screen_name
        status_id = status.id

    # entities provide structured data from Tweets including resolved URLs,
    # media, hashtags and mentions without having to parse the text to extract
    # that information. We are only interested in the text for now.
        tweet_response(status.text, username, status_id)
        print(status.text)


myStreamListener = BotStreamer()

#  Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
print("initialised stream")
stream.filter(track=['@BSORNOT1'])
