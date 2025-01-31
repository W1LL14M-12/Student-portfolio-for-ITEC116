Activity #3: Working with JSON – Detailed Post API
This activity involves working with JSON data and building a FastAPI endpoint that retrieves user posts along with their associated comments. The API fetches posts based on a given userID and structures the response in a clear format.

Folder: detailed_post_api/
Overview
Framework: FastAPI
Endpoint: /detailed_post/{userID}
Method: GET
Functionality:
Retrieves all posts made by a specific user.
Includes all comments for each post.
Ensures proper key-value naming for clarity.
Setup Instructions
Clone the Required GitHub Repository

sh
Copy
Edit
git clone https://github.com/jpcanamaque/itec116_it4e_lab.git
cd itec116_it4e_lab/lab3
Set Up Virtual Environment and Install Dependencies

sh
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate  # For Windows
pip install -r requirements.txt
Run the API

sh
Copy
Edit
uvicorn main:app --reload
How the API Works
The user makes a GET request to /detailed_post/{userID}.
The API fetches all posts belonging to the given userID.
It retrieves all comments related to each post.
The API returns a JSON response with structured data.
Example API Calls and Responses
Request: GET /detailed_post/1
Response Format (Example):
json
Copy
Edit
[
  {
    "post_id": 101,
    "title": "First Post",
    "body": "This is the first post content.",
    "comments": [
      {
        "comment_id": 1,
        "name": "User A",
        "comment": "Great post!"
      },
      {
        "comment_id": 2,
        "name": "User B",
        "comment": "Thanks for sharing."
      }
    ]
  },
  {
    "post_id": 102,
    "title": "Second Post",
    "body": "Another interesting post.",
    "comments": []
  }
]
Output Expectations
The expected output follows the structure shown in expected_output.json in the GitHub repository.

Required Files in Submission
main.py – Updated API logic based on the provided repository.
requirements.txt – (Optional) List of dependencies used in the project.
