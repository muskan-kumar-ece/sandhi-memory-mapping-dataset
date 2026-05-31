import requests
import json
import os

subreddits = [
    "Anxiety",
    "GetStudying",
    "IndianAcademia",
    "selfimprovement"
]

all_posts = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Beginning Reddit Scraping...")

for subreddit in subreddits:
    print(f"Scraping r/{subreddit}...")
    url = f"https://www.reddit.com/r/{subreddit}.json?limit=50"
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            posts_added = 0
            for post in data["data"]["children"]:
                post_data = post["data"]
                # Skip stickied posts or posts without content
                if post_data.get("stickied", False):
                    continue
                
                title = post_data.get("title", "")
                body = post_data.get("selftext", "")
                
                if not title and not body:
                    continue
                    
                all_posts.append({
                    "subreddit": subreddit,
                    "title": title,
                    "body": body,
                    "score": post_data.get("score", 0)
                })
                posts_added += 1
            print(f"Successfully collected {posts_added} posts from r/{subreddit}.")
        else:
            print(f"Failed to fetch r/{subreddit} (HTTP {response.status_code})")
    except Exception as e:
        print(f"Error scraping r/{subreddit}: {e}")

print(f"\nTotal posts collected: {len(all_posts)}")

raw_data_dir = r"c:\workflow\sandhidataset\sandhi_dataset_pipeline\raw_data"
os.makedirs(raw_data_dir, exist_ok=True)

output_path = os.path.join(raw_data_dir, "raw_posts.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_posts, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
