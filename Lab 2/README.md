Activity #2: Working with HTTP Actions and API Parameters – To-Do List API
This activity builds on a sample FastAPI project by implementing a To-Do List API. The API allows users to manage tasks using standard HTTP methods (GET, POST, PATCH, DELETE) while ensuring proper validation and error handling.

Folder: todo_list_api/
Overview
Framework: FastAPI
Database Simulation: A list (task_db) acts as a temporary database to store tasks.
Endpoints:
GET /tasks/{task_id} – Retrieve a task by its ID.
POST /tasks – Add a new task.
PATCH /tasks/{task_id} – Update an existing task.
DELETE /tasks/{task_id} – Remove a task.
Validation: Every input is validated (null checks, negative values, division by zero, etc.).
Response Format:
Success: {"status": "ok"}
Errors: {"error": "<specific error message>"}
Simulated Database
At the start, the API has the following default task stored in task_db:

json
Copy
Edit
[
  {
    "task_id": 1,
    "task_title": "Laboratory Activity",
    "task_desc": "Create Lab Act 2",
    "is_finished": false
  }
]
How the API Works
Get a Task (GET /tasks/{task_id})

Returns the details of a specific task.
If task_id is not found, returns {"error": "Task not found"}.
Example Request:

bash
Copy
Edit
GET /tasks/1
Response:

json
Copy
Edit
{
  "task_id": 1,
  "task_title": "Laboratory Activity",
  "task_desc": "Create Lab Act 2",
  "is_finished": false
}
Create a New Task (POST /tasks)

Adds a new task to task_db.
Required fields: task_title and task_desc.
Returns {"status": "ok"} on success.
Example Request:

json
Copy
Edit
{
  "task_title": "New Task",
  "task_desc": "Complete API project"
}
Response:

json
Copy
Edit
{"status": "ok"}
Update a Task (PATCH /tasks/{task_id})

Updates the details of a task.
Can modify task_title, task_desc, or is_finished.
If task_id is invalid, returns {"error": "Task not found"}.
Example Request:

json
Copy
Edit
{
  "is_finished": true
}
Response:

json
Copy
Edit
{"status": "ok"}
Delete a Task (DELETE /tasks/{task_id})

Removes a task from task_db.
If task_id is invalid, returns {"error": "Task not found"}.
Example Request:

bash
Copy
Edit
DELETE /tasks/1
Response:

json
Copy
Edit
{"status": "ok"}
Error Handling and Validation
Invalid Input Handling:
task_id must be a valid integer.
task_title and task_desc must not be empty.
Edge Cases Covered:
Handling negative numbers.
Preventing duplicate task_id.
Avoiding operations on non-existent tasks.
How to Run the API
Install FastAPI and Uvicorn (if not installed):
sh
Copy
Edit
pip install fastapi uvicorn
Run the API:
sh
Copy
Edit
uvicorn main:app --reload
Use a browser or API testing tool (like Postman) to interact with the endpoints.
