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

def post_image_and_video_v2(message, image_path, video_path):
    try:
        image_media = api.media_upload(image_path)
        video_media = api.media_upload(video_path, media_category='tweet_video')
        client.create_tweet(text=message, media_ids=[image_media.media_id, video_media.media_id])
        print(f"Message with image and video posted: {message}, Image: {image_path}, Video: {video_path}")
    except tweepy.TweepyException as e:
        print(f"Failed to post image and video: {e}")

# Example usage
post_image_and_video_v2("Here are both an image and a video!", r"C:\path\to\your\image.jpg", r"C:\path\to\your\video.mp4")

