from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import databases
import sqlalchemy

# SQLite database
DATABASE_URL = "sqlite:///./data/items.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Table definition
items_table = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String),
)

# SQLAlchemy engine
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

# FastAPI app
app = FastAPI(title="SQLite CRUD API")

# Pydantic models
class ItemIn(BaseModel):
    name: str
    description: str | None = None

class Item(ItemIn):
    id: int

# Startup & shutdown events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# CRUD Endpoints
@app.post("/items/", response_model=Item)
async def create_item(item: ItemIn):
    query = items_table.insert().values(name=item.name, description=item.description)
    item_id = await database.execute(query)
    return {**item.dict(), "id": item_id}

@app.get("/items/", response_model=List[Item])
async def read_items():
    query = items_table.select()
    return await database.fetch_all(query)

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items_table.select().where(items_table.c.id == item_id)
    item = await database.fetch_one(query)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: ItemIn):
    query = items_table.update().where(items_table.c.id == item_id).values(
        name=updated_item.name, description=updated_item.description
    )
    await database.execute(query)
    return {**updated_item.dict(), "id": item_id}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items_table.delete().where(items_table.c.id == item_id)
    await database.execute(query)
    return {"detail": "Item deleted"}