#requests

import requests


#get requests
def fetch_data():
    response = requests.get(
#JSONplaceholder API
     "https://jsonplaceholder.typicode.com/posts/1"
    )
#response
    if response.status_code == 200:
        return response.json()

    return {}

def save_data(post):
    with open("post.txt", "w") as file:
              file.write(f"Title: {post.get('title', 'No title found')}\n")
              file.write(f"Body: {post.get('body', 'No body found')}\n")
    



if __name__ == "__main__":
    post = fetch_data()

    if post:
        save_data(post)
        print("Post saved successfully.")
    else:
        print("Failed to fetch post.")

   