import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f"Failed to fetch users: HTTP {response.status_code}")
        return []

def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        return posts
    else:
        print(f"Failed to fetch posts: HTTP {response.status_code}")
        return []

if __name__ == "__main__":
    users = fetch_users()

    for user in users:
        # print(f"– {user['name']} (username: {user['username']}, email: {user['email']})")
        print(f"{user['id']}: {user['username']}")

    posts = fetch_post()
    user_posts = {user['id'] : [] for user in users}

    for post in posts:
        user_id = post['userId']
        user_posts[user_id].append(post['id'])

    print(user_posts)