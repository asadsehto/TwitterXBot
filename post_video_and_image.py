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

def post_video_and_image_v2(message, video_path, image_path):
    try:
        video_media = api.media_upload(video_path, media_category='tweet_video')
        image_media = api.media_upload(image_path)
        client.create_tweet(text=message, media_ids=[video_media.media_id, image_media.media_id])
        print(f"Message with video and image posted: {message}, Video: {video_path}, Image: {image_path}")
    except tweepy.TweepyException as e:
        print(f"Failed to post video and image: {e}")

# Example usage
post_video_and_image_v2("Here is a video followed by an image!", r"C:\path\to\your\video.mp4", r"C:\path\to\your\image.jpg")
