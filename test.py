import praw

reddit = praw.Reddit(
    client_id="kOzq249feXHiuh3Y4moM8aC1sVaKHA",
    client_secret="DDScYrlvPYFopqlOS3IReQ",
    user_agent="kaggle:reddit-test:v1.0 (by u/test_user)"
)

for post in reddit.subreddit("netsec").hot(limit=5):
    print(post.title)
