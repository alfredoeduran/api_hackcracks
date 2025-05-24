from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from database import get_db_connection
from crud import create_item, get_items, get_item, update_item, delete_item

app = FastAPI(title="FastAPI MySQL Railway API")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI MySQL Railway API"}

@app.post("/items/", response_model=Item)
async def create_item_endpoint(item: Item):
    return create_item(item)

@app.get("/items/", response_model=List[Item])
async def read_items():
    return get_items()

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item_endpoint(item_id: int, item: Item):
    updated_item = update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item_endpoint(item_id: int):
    if not delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 