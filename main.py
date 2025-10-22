from typing import Annotated, Literal

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from schemas.item import FilterParams, PathParams, UpdateItem
from controllers import category, item, auth

app = FastAPI()

app.include_router(category.router)
app.include_router(item.router)
app.include_router(auth.router)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query(alias="item-query", title="Query string", deprecated=True,
                                                          description="Query string for the items to search in the database that have a good match",
                                                          )] = None):
    query_items = {"q": q}
    return query_items


@app.get("/items/{item_id}/{path_item}")
async def read_item(path_item: Annotated[int, Path(title="The ID of path", qe=1, min_length=5, max_length=50)], item_id: int, needly: str,
                    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    return {"item_id": item_id, "q": q, "needly": needly, "path_item": path_item}


@app.post("/items")
async def create_item(item: Item | None = None):
    return {"item": item}


@app.get("/items/filter/{id}")
async def filter_items(filter_query: Annotated[FilterParams, Query()], path_params: Annotated[PathParams, Path()]):
    return {"filter": filter_query, "path_params": path_params}

@app.patch('/items')
async def update_item(item: Annotated[UpdateItem, Body()]):
    return {"item": item}