from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
]

class Product(BaseModel):
    name: str
    price: float

@app.get("/products", status_code=200)
def get_products():
    return products

@app.get("/products/{product_id}", status_code=200)
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return {"error": "Product not found"}, 404
    return product

@app.post("/products", status_code=201)
def create_product(product: Product):
    if not product.name:
        return {"error": "name is required"}, 400
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }
    products.append(new_product)
    return new_product