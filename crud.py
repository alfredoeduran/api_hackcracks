from database import get_db_connection
from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

def create_item(item: Item) -> Item:
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO items (name, description) VALUES (%s, %s)"
            cursor.execute(query, (item.name, item.description))
            connection.commit()
            item.id = cursor.lastrowid
            return item
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return None

def get_items() -> List[Item]:
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM items")
            items = cursor.fetchall()
            return [Item(**item) for item in items]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return []

def get_item(item_id: int) -> Optional[Item]:
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
            item = cursor.fetchone()
            return Item(**item) if item else None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return None

def update_item(item_id: int, item: Item) -> Optional[Item]:
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE items SET name = %s, description = %s WHERE id = %s"
            cursor.execute(query, (item.name, item.description, item_id))
            connection.commit()
            if cursor.rowcount > 0:
                item.id = item_id
                return item
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return None

def delete_item(item_id: int) -> bool:
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False 