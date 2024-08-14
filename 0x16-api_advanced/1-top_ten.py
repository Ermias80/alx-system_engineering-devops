#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the subreddit exists
    if response.status_code == 404:
        print("None")
        return

    # Print the status code for debugging
    print(f"Status code: {response.status_code}")  # Optional for debugging

    # Attempt to parse the JSON response
    try:
        results = response.json().get("data")
        for c in results.get("children"):
            print(c.get("data").get("title"))
    except ValueError:
        print("None")
