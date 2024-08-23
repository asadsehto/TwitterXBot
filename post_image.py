import tweepy

# Add your API keys here
bearer_token = 'your_bearer_token'
api_key = 'your_api_key'
api_key_secret = 'your_api_key_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_key_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def post_image_v2(message, image_path):
    try:
        media = api.media_upload(image_path)
        client.create_tweet(text=message, media_ids=[media.media_id])
        print(f"Message with image posted: {message}, Image: {image_path}")
    except tweepy.TweepyException as e:
        print(f"Failed to post image: {e}")

# Example usage
post_image_v2("Check out this image!", r"C:\path\to\your\image.jpg")
