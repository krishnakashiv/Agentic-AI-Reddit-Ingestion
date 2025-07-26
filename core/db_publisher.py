import sqlite3
import json

def publish_to_db(post_id, summary, full_record, db_path="reddit_posts.db"):
    print(f"Publishing post {post_id} to database...")

