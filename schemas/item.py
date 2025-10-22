from typing import Literal

from pydantic import Field, BaseModel


class FilterParams(BaseModel):
    limit: int = Field(50, gt=0, lt=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

class PathParams(BaseModel):
    id: int = Field(None, gt=0)

class UpdateItem(BaseModel):
    id: int = Field(None, gt=0)
    name: str = Field()
    description: str = Field(max_length=100, title="Description of item")
    price: float = Field( gt=0, title="Price of item")

