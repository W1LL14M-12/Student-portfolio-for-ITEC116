import requests
import json
import os
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Fetch all posts or a specific post by postId
@app.get("/posts/")
def get_posts(postId: Optional[int] = None):
    if postId is None:
        # Fetch all posts
        posts = requests.get('https://jsonplaceholder.typicode.com/posts')
        response = posts.json()
    else:
        # Fetch a specific post by postId
        posts = requests.get(f'https://jsonplaceholder.typicode.com/posts/{postId}')
        response = posts.json()
    
    return response

# Fetch all comments or comments for a specific post by postId
@app.get("/comments/")
def get_comments(postId: Optional[int] = None):
    if postId is None:
        # Fetch all comments
        comments = requests.get('https://jsonplaceholder.typicode.com/comments')
        response = comments.json()
    else:
        # Fetch comments for a specific post by postId
        comments = requests.get(f'https://jsonplaceholder.typicode.com/comments?postId={postId}')
        response = comments.json()
    
    return response

# Example API to format posts for a specific user
@app.get("/formatted_posts/{userID}")
def get_formatted_posts(userID: int):
    posts = get_posts()
    data = {"userID": userID, "posts": []}
    
    # Filter posts by userID and format the response
    for post in posts:
        if post['userId'] == userID:
            data["posts"].append({
                "post_title": post["title"],
                "post_body": post["body"],
            })
    return data

# Example API to format comments for a specific post
@app.get("/formatted_comments/{postID}")
def get_formatted_comments(postID: int):
    comments = get_comments(postId=postID)
    data = {"post_id": postID, "comments": []}
    
    # Filter comments by postID and format the response
    for comment in comments:
        data["comments"].append({
            "commenter_email": comment["email"],
            "commenter_name": comment["name"],
            "comment": comment["body"],
        })
    return data

# New API for fetching posts of a specific user and their comments
@app.get("/detailed_post/{userID}")
def get_detailed_post(userID: int):
    # Fetch all posts
    posts = get_posts()

    # Structure to hold the user's posts with their respective comments
    user_posts_with_comments = {
        "userID": userID,
        "posts": []
    }

    # Filter posts by userID
    for post in posts:
        if post['userId'] == userID:
            # Fetch comments for each post
            comments = get_comments(postId=post['id'])
            
            # Append post details with comments
            user_posts_with_comments["posts"].append({
                "post_title": post["title"],
                "post_body": post["body"],
                "comments": comments  # Directly add the comments to the post
            })

    return user_posts_with_comments

# New API to return the JSON data from 'expected_output.json'
@app.get("/get_json_output/")
def get_json_output():
    try:
        # Print the current working directory for debugging
        print("Current Directory:", os.getcwd())

        # Load the JSON data from the file
        with open('expected_output.json', 'r') as file:
            data = json.load(file)
        
        return data

    except Exception as e:
        # Return the error message as a response for debugging
        return {"error": str(e)}