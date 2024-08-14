#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    # Define the URL and headers for the request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyApp'}

    try:
        # Perform the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and the status code is 200
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json().get("data")
            if data:
                # Return the number of subscribers
                return data.get("subscribers", 0)
        # Return 0 if the request was unsuccessful or if data is not available
        return 0

    except requests.RequestException:
        # Handle any request exceptions (e.g., network errors)
        return 0
