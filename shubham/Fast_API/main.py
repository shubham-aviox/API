from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, Query

class Item(BaseModel):
   name: str
   description: Optional[str] = None
   price: float
   tax: Optional[float] = None
   tags: list = []


app = FastAPI()

# @app.get('/items/{item_id}')
# def func(item_id: int):
#    return {'item_id': item_id}

# @app.get('/users/me')
# def read_user_me():
#    return {'user_id': 'the current user'}

# @app.get('/users/{user_id}')
# def read_user(user_id: str):
#    return {'user_id': user_id}

# @app.post('/items')
# def create_item(item: Item):
#    item_dict = item.dict()
#    if item.tax:
#       price_with_tax = item.price + item.tax
#       item.dict.update({'price_with_tax': price_with_tax})
#    return item


# @app.put('/items/{item_id}')
# def create_item(item_id: int, item: Item):
#    return {'item_id': item_id, **item.dict()}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get('/items')
# def read_item(skip: int=0, limit: int=10):
#    return fake_items_db[skip: skip + limit]

# @app.get('/items/{item_id}')
# def read_item(item_id: str, q: Optional[str]=None):
#    if q:
#       return {'item_id': item_id, 'q': q}
#    return {'item_id': item_id}

# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Optional[List[str]] = Query('djfhskj')):
#     query_items = {"q": q}
#     return query_items


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
