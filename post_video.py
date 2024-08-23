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

def post_video_v2(message, video_path):
    try:
        media = api.media_upload(video_path, media_category='tweet_video')
        client.create_tweet(text=message, media_ids=[media.media_id])
        print(f"Message with video posted: {message}, Video: {video_path}")
    except tweepy.TweepyException as e:
        print(f"Failed to post video: {e}")

# Example usage
post_video_v2("Check out this video!", r"C:\path\to\your\video.mp4")
