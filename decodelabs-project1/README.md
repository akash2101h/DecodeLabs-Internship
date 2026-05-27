# DecodeLabs Internship - Project 1

This is my first project as a backend development intern at DecodeLabs. 
I built a simple REST API using FastAPI and Python.

## What I built
I built a REST API which is basically a server that listens for requests and responds with data.

Specifically:
Someone visits /products → the server responds with a list of products
Someone visits /products/1 → the server responds with only that one product
Someone sends a POST request to /products → the server creates a new product and saves it

All responses are in JSON format and the server runs locally on port 8000
The server is stateless — meaning it doesn't remember anything between requests, every request is treated fresh.

## Technologies Used
- Python
- FastAPI
- Uvicorn

## How to run this project
It runs locally on your computer — meaning only you can access it right now.
When you ran:
```
uvicorn main:app --reload
```

```
http://127.0.0.1:8000/docs
```
You can test all endpoints directly from the browser without any extra tools.

---

## API Routes
GET /products — returns all products
GET /products/{id} — returns a single product by ID
POST /products — creates a new product

## What I learned
Before this project I had no idea what a REST API was. I learned that GET is used to fetch data and POST is used to create new data. I also learned that every response should return a proper status code like 200 for success and 404 when something is not found. The concept of stateless server was new to me it means the server doesn't remember anything between requests.