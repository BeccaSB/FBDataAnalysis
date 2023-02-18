import facebook
import requests
import json
from collections import Counter

# Replace with your access token and user ID
access_token = '<YOUR_ACCESS_TOKEN>'
user_id = '<USER_ID>'

graph = facebook.GraphAPI(access_token)
posts = graph.get_connections(user_id, 'posts')

# Save the data to a file
with open('posts.json', 'w') as f:
    f.write(json.dumps(posts))

# Load the data from the file
with open('posts.json', 'r') as f:
    posts = json.load(f)

# Load the data from the file
with open('posts.json', 'r') as f:
    posts = json.load(f)

# Remove duplicates
unique_posts = []
for post in posts['data']:
    if post not in unique_posts:
        unique_posts.append(post)

# Save the data to a new file
with open('cleaned_posts.json', 'w') as f:
    f.write(json.dumps(unique_posts))


# Load the data from the file
with open('cleaned_posts.json', 'r') as f:
    posts = json.load(f)

# Extract the year and month from each post
post_dates = [post['created_time'][:7] for post in posts]

# Count the frequency of each month
frequency = Counter(post_dates)

# Print the results
for month, count in frequency.most_common():
    print(f'{month}: {count} posts')