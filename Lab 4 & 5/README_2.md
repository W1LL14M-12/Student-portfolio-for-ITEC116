Here's a draft of the README section for Activity #5:  

---

### Activity #5: Deploying API in the Cloud  

This activity extends **Activity #4** by deploying the **Advanced To-Do List API** to a cloud platform, **Render**. The deployed API should be accessible via a public URL and maintain all features from the previous activity, including **API versioning, authentication, and exception handling**.  

#### **Folder: `deployed_todo_api/`**  

#### **Overview**  
- **Framework:** FastAPI  
- **Deployment Platform:** Render (https://render.com/)  
- **Key Features:**  
  - Cloud-deployed API  
  - Maintains **apiv1** (basic API) and **apiv2** (enhanced API with authentication and exception handling)  
  - API key stored securely in environment variables on Render  
  - Uses **proper HTTP status codes** for success and error handling  

---

### **Setup and Deployment Guide**  

#### **1. Clone the Repository**  
   ```sh
   git clone <your_github_repo_url>
   cd deployed_todo_api
   ```

#### **2. Prepare API for Deployment**  
1. Ensure **all dependencies** are listed in `requirements.txt`:  
   ```sh
   pip freeze > requirements.txt
   ```  
2. Add a **Procfile** (if not already present):  
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```  
3. Push the latest code to GitHub:  
   ```sh
   git add .
   git commit -m "Prepare API for deployment"
   git push origin main
   ```  

#### **3. Deploy to Render**  
1. Go to **[Render.com](https://dashboard.render.com/)** and create a new **Web Service**.  
2. Connect your GitHub repository.  
3. Set the **Build Command**:  
   ```sh
   pip install -r requirements.txt
   ```  
4. Set the **Start Command**:  
   ```sh
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```  
5. Add an **Environment Variable** for the API Key:  
   ```
   LAB4_API_KEY=my_api_key
   ```
   (This must match the API key used in your local `.env` file).  
6. Deploy and get the **public API URL** (format: `itec116_<surname>.onrender.com`).  

---

### **Endpoints and Features**  

1. **Versioning Implementation**  
   - `apiv1` – Basic API version.  
   - `apiv2` – Improved API with authentication and error handling.  

2. **Authentication – API Key Validation**  
   - Each request must include a valid **API Key**.  
   - If the key is missing or incorrect, the API will return:  
     ```json
     {"error": "Invalid API Key"}
     ```

3. **Improved Exception Handling and Status Codes**  
   - `404` – Task not found (GET, PATCH, DELETE).  
   - `204` – No tasks available / Task updated or deleted.  
   - `201` – Task added successfully.  
   - `200` – General success responses.  

---

### **Example API Calls (Cloud Deployed Version)**  

- **Retrieve Task (`GET` /apiv2/tasks/{task_id})**  
  ```
  GET https://itec116_<surname>.onrender.com/apiv2/tasks/1
  ```
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

- **Add a Task (`POST` /apiv2/tasks) – Returns `201`**  
  ```json
  {"status": "ok"}
  ```

- **Update a Task (`PATCH` /apiv2/tasks/{task_id}) – Returns `204`**  
  ```json
  {"status": "ok"}
  ```

- **Delete a Task (`DELETE` /apiv2/tasks/{task_id}) – Returns `204`**  
  ```json
  {"status": "ok"}
  ```

- **No Tasks Found (`204`)**  
  ```json
  {"error": "No tasks available"}
  ```

---

### **Security Measures Implemented**  
✅ API key authentication via **Render Environment Variables**  
✅ **.env file excluded** from GitHub (via `.gitignore`)  
✅ Proper **HTTP status codes** for API responses  

---

### **Required Submission Files**  
- **GitHub Repository** with:  
  - Updated `main.py`  
  - `.gitignore` file (to exclude `.env`)  
  - `requirements.txt` (dependencies)  
  - `Procfile` (for deployment)  
- **Deployed API Link on Render**  
  ```
  https://itec116_<surname>.onrender.com
  ```
- **Private API Key Submission**  
  ```
  LAB4_API_KEY=my_api_key
  ```
  - This must match the key set in **Render Environment Variables**.  

---

Let me know if you need any modifications before adding this to the README file! 🚀
