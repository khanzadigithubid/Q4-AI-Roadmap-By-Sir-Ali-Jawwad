Step 1: Create Project Directory and Switch to it
Create a new project directory and navigate into it:

uv init fastdca-p1
cd fastdca-p1

Step 2: Create and Activate the Virtual Environment
On macOS/Linux:

uv venv
source .venv/bin/activate
On Windows:


uv venv
.venv\Scripts\activate
Note: With Python 3.11+, you may not need to manually activate the virtual environment thanks to PEP 582.

Step 3: Install Dependencies
You will need FastAPI, Uvicorn, and testing dependencies like pytest and pytest-asyncio:

Install the required dependencies:

uv add "fastapi[standard]"
To add development dependencies like pytest:

uv add --dev pytest pytest-asyncio
This will update your pyproject.toml file with the necessary packages.

Step 4: Create Your First API Route
Edit your main.py file to define your first API routes.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
Step 5: Run the Server
To run the server:

Development Mode: Use FastAPI's development command:

fastapi dev main.py
This runs the app with automatic reloading in development mode.

Alternatively: You can use Uvicorn directly:

uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Explanation of fastapi dev main.py:

FastAPI: The web framework.

dev: A subcommand for running FastAPI in development mode (auto-reloads the server on changes).

main.py: The Python file with your FastAPI app instance.

Step 6: Test Your APIs
Once the server is running, open your browser and visit:

Root endpoint: http://localhost:8000

Items endpoint: http://localhost:8000/items/5?q=somequery

This will return the following JSON responses:

For /:

{"Hello": "World"}
For /items/{item_id} (with item ID 5):

{"item_id": 5, "q": "somequery"}
Step 7: Interactive API Docs
FastAPI automatically generates interactive API docs for your project. Open the following URL in your browser:

Swagger UI: http://localhost:8000/docs