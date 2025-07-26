import json
import csv

def consolidate(post_id, summary, links, link_details):
    return {
        "post_id": post_id,
        "summary": summary,
        "links": links,
        "link_data": link_details
    }

def save_to_json(data, path="output/posts.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def save_to_csv(data, path="output/posts.csv"):
    keys = data[0].keys()
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
