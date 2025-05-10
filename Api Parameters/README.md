FastAPI Item Management API
A simple REST API built with FastAPI for managing items with various parameters and validation. 🛠️

Features ✨
Path parameters with validation 🔍

Query parameters with validation 📝

Request body validation using Pydantic models 🛡️

Optional parameters support 🆗

Built-in API documentation 📚

Requirements 📋
Python 3.11 or higher 🐍

FastAPI 🚀

Uvicorn (included with FastAPI standard dependencies) 🔥

Installation 🔧
Clone the repository 📂

Create a virtual environment:


python -m venv .venv
Activate the virtual environment:

Windows:
.venv\Scripts\activate
Unix/MacOS:

source .venv/bin/activate
Install dependencies:

pip install -e .
Running the Application 🚀
Start the server with:


uvicorn main:app --reload
The API will be available at http://localhost:8000

API Documentation 📖
Once the server is running, you can access:

Interactive API documentation (Swagger UI): http://localhost:8000/docs 🔍

Alternative API documentation (ReDoc): http://localhost:8000/redoc 📘

API Endpoints 📡
1. Get Item by ID
Endpoint: GET /items/{item_id}

Path Parameters:

item_id (integer, required): Must be greater than or equal to 1

Response: Returns the item ID

2. Get List of Items
Endpoint: GET /items/

Query Parameters:

q (string, optional): Search query (3-50 characters)

skip (integer, optional): Number of items to skip (default: 0)

limit (integer, optional): Maximum number of items to return (default: 10)

Response: Returns query parameters and pagination info

3. Update Item
Endpoint: PUT /items/{item_id}

Path Parameters:

item_id (integer, required): Must be greater than or equal to 1

Query Parameters:

q (string, optional): Search query (minimum 3 characters)

Request Body (optional):

{
  "name": "string",
  "description": "string (optional)",
  "price": "float"
}
Response: Returns updated item information

Example Usage 💻
Get Item by ID

curl http://localhost:8000/items/1

Get Items with Query Parameters

curl "http://localhost:8000/items/?q=test&skip=0&limit=10"

Update Item

curl -X PUT "http://localhost:8000/items/1?q=test" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Item", "description": "This is a test item", "price": 29.99}'

License 📜
This project is open source and available under the MIT License. Feel free to use, modify, and distribute it! 🎉
