Activity #1: Introduction to FastAPI – Factorial API
This activity is an introduction to FastAPI, a modern web framework for building APIs with Python. The goal is to create an API that calculates the factorial of a given number using a while loop.

Folder: factorial_api/
Overview
Framework: FastAPI
Endpoint: /factorial/{starting_number}
Logic:
The endpoint receives a number (starting_number) as input.
It calculates the factorial of the number using a while loop.
If the input is 0, the API returns {"result": false}.
Otherwise, it returns the computed factorial in JSON format.
How the Factorial is Computed
The factorial of a number n (denoted as n!) is the product of all positive integers from 1 to n.
For example:

5! = 5 × 4 × 3 × 2 × 1 = 120
3! = 3 × 2 × 1 = 6
1! = 1
0! is a special case that usually equals 1, but in this activity, the API returns false.
How the API Works
The user sends a request to /factorial/{starting_number}.
The API checks if the number is 0. If so, it returns {"result": false}.
If the number is greater than 0, the API computes the factorial using a while loop.
The API returns the factorial result in JSON format.
Example API Calls and Responses
Request: GET /factorial/5
Response: {"result": 120}
Request: GET /factorial/0
Response: {"result": false}
How to Run the API
Install FastAPI and Uvicorn (if not installed):
sh
Copy
Edit
pip install fastapi uvicorn
Run the FastAPI application:
sh
Copy
Edit
uvicorn main:app --reload
Access the API using a web browser or tools like Postman.
Additional Notes
The factorial calculation uses a while loop instead of recursion to demonstrate looping structures in Python.
The API follows RESTful principles, making it easy to integrate with other applications.
The response format is JSON for better readability and compatibility with frontend applications.
