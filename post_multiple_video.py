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

def post_multiple_videos_v2(message, video_paths):
    try:
        media_ids = [api.media_upload(video, media_category='tweet_video').media_id for video in video_paths]
        client.create_tweet(text=message, media_ids=media_ids)
        print(f"Message with multiple videos posted: {message}, Videos: {video_paths}")
    except tweepy.TweepyException as e:
        print(f"Failed to post multiple videos: {e}")

# Example usage
post_multiple_videos_v2("Check out these videos!", [r"C:\path\to\your\video1.mp4", r"C:\path\to\your\video2.mp4"])
