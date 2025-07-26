import praw
from dotenv import load_dotenv
import os

load_dotenv()
print("Client ID:", os.getenv("REDDIT_CLIENT_ID"))
print("Client Secret:", os.getenv("REDDIT_CLIENT_SECRET"))
print("Username:", os.getenv("REDDIT_USERNAME"))
print("Password:", "******" if os.getenv("REDDIT_PASSWORD") else "NOT SET")
def get_reddit_client():
    print("Initializing Reddit client...")
    
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="script:reddit-ingestion-pipeline:v1.0 (by /u/krishkash)",
    )

def fetch_posts(subreddit_name="netsec", limit=50):
    reddit = get_reddit_client()
    return list(reddit.subreddit(subreddit_name).new(limit=limit))
