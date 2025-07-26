from core.reddit_ingestor import fetch_posts
from agents.post_relevancy_agent import is_post_relevant
from agents.post_analyzer_agent import analyze_post
from agents.link_analyzer_agent import analyze_link
from agents.consolidator_agent import consolidate, save_to_json
from core.db_publisher import publish_to_db

all_data = []

for post in fetch_posts("netsec", limit=25):
    print("\n\n\n")

    title = post.title
    body = post.selftext or ""
    post_id = post.id
    post_url = post.url

    print(f"Processing Post ID: {post_id}, Title: {title}")
    print(f"Body: {body[:100]}...")  # Print first 100 characters of body for brevity

    # Step 1: Relevancy check
    if not is_post_relevant(title, body):
        continue

    # Step 2: Analyze post (summary + extract links from body)
    summary, links = analyze_post(title, body)

    # Step 3: If post has no body but contains a non-Reddit link → analyze that link
    if not body.strip() and post_url and "reddit.com" not in post_url.lower():
        print(f"Adding post URL to links since body is empty and URL is external: {post_url}")
        links.append(post_url)

    # Step 4: Analyze all links
    link_data = [analyze_link(url) for url in links]

    print(f"Post ID: {post_id}, Summary: {summary}, Links: {links}")

    # Step 5: Consolidate and save
    record = consolidate(post_id, summary, links, link_data)
    print(f"Consolidated Record: {record}")
    publish_to_db(post_id, summary, record)
    all_data.append(record)

# Final: save output to JSON
save_to_json(all_data)
