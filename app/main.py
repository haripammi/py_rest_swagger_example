from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple CRUD API")

# In-memory "database"
items = []

class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Create
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for i in items:
        if i.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

# Read all
@app.get("/items/", response_model=List[Item])
def read_items():
    return items

# Read one
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")