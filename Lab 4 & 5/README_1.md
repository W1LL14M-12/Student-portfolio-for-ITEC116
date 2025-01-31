Here's a draft of the README section for Activity #4:  

---

### Activity #4: Advanced API Implementation – Versioning, Authentication, and Exception Handling  

This activity expands on the **To-Do List API** from Activity #2 by implementing **API versioning, authentication, proper HTTP exception handling, and best practices for environment variables**.  

#### **Folder: `advanced_todo_api/`**  

#### **Overview**  
- **Framework:** FastAPI  
- **Key Features:**  
  - **API Versioning:**  
    - `apiv1` – Original To-Do List API (from Activity #2).  
    - `apiv2` – Improved version with exception handling, authentication, and status codes.  
  - **Authentication:**  
    - API key stored in a `.env` file (excluded from the repository using `.gitignore`).  
  - **Exception Handling:**  
    - Returns proper error responses for invalid requests.  
  - **Improved HTTP Status Codes:**  
    - `201` – Task added successfully.  
    - `204` – Task updated, deleted, or if no tasks are found.  
    - `404` – Task not found when retrieving, updating, or deleting.  
    - `200` – Default for all other cases.  

#### **Setup Instructions**  

1. **Clone the Repository**  
   ```sh
   git clone <your_github_repo_url>
   cd advanced_todo_api
   ```  

2. **Set Up Virtual Environment and Install Dependencies**  
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # For Mac/Linux
   .venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```  

3. **Create a `.env` File and Add an API Key**  
   - Inside the `advanced_todo_api` folder, create a new `.env` file:  
     ```sh
     touch .env
     ```  
   - Add your API key to the file (example format):  
     ```
     LAB4_API_KEY=my_api_key
     ```  
   - The `.env` file is **not included in the repository** (protected via `.gitignore`).  

4. **Run the API**  
   ```sh
   uvicorn main:app --reload
   ```  

#### **Endpoints and Features**  

1. **Versioning Implementation**  
   - **API v1 (apiv1):** Basic To-Do List API from Activity #2.  
   - **API v2 (apiv2):** Improved version with authentication, error handling, and better status codes.  

2. **Authentication – API Key Validation**  
   - Each request requires an API key.  
   - The key is retrieved from environment variables and validated in API calls.  
   - If the key is missing or incorrect, the response will be:  
     ```json
     {"error": "Invalid API Key"}
     ```

3. **Improved Exception Handling**  
   - **Task Not Found (`404`)**:  
     - When accessing, updating, or deleting a non-existent task.  
   - **Empty Task List (`204`)**:  
     - When there are no tasks to display.  
   - **Success Codes:**  
     - `201` for successful task creation.  
     - `204` for task updates and deletions.  
     - `200` for general success responses.  

#### **Example API Calls and Responses**  

- **Retrieve Task (GET /apiv2/tasks/{task_id})**  
  - If task exists:  
    ```json
    {
      "task_id": 1,
      "task_title": "Complete API",
      "task_desc": "Implement versioning",
      "is_finished": false
    }
    ```
  - If task does not exist (`404`):  
    ```json
    {"error": "Task not found"}
    ```

- **Add a Task (POST /apiv2/tasks) – Returns `201`**  
  ```json
  {"status": "ok"}
  ```

- **Update a Task (PATCH /apiv2/tasks/{task_id}) – Returns `204`**  
  ```json
  {"status": "ok"}
  ```

- **Delete a Task (DELETE /apiv2/tasks/{task_id}) – Returns `204`**  
  ```json
  {"status": "ok"}
  ```

- **No Tasks Found (`204`)**  
  ```json
  {"error": "No tasks available"}
  ```

#### **Security Measures Implemented**  
✅ API key authentication via `.env`  
✅ `.gitignore` prevents exposing sensitive data  
✅ Proper HTTP status codes for clear API responses  

#### **Required Submission Files**  
- **GitHub Repository** with:  
  - Updated `main.py`  
  - `.gitignore` file (to exclude `.env`)  
  - (Optional) `requirements.txt`  
- **Private API Key Submission**  
  - Example format:  
    ```
    LAB4_API_KEY=my_api_key
    ```
  - This must be sent privately (not included in the repository).  

---

Let me know if you need any modifications before adding this to the README file! 🚀
