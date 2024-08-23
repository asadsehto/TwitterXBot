import tweepy

# Add your API keys here
bearer_token = 'your_bearer_token'
api_key = 'your_api_key'
api_key_secret = 'your_api_key_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Create a client instance using tweepy.Client (API v2)
client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_key_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

def post_message_v2(message):
    try:
        client.create_tweet(text=message)
        print("Message posted:", message)
    except tweepy.TweepyException as e:
        print(f"Failed to post message: {e}")

# Example usage
post_message_v2("Hello Twitter! This is a simple message.")
