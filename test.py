import praw

reddit = praw.Reddit(
    client_id="XXX",
    client_secret="XX",
    user_agent="kaggle:reddit-test:v1.0 (by u/test_user)"
)

for post in reddit.subreddit("netsec").hot(limit=5):
    print(post.title)
