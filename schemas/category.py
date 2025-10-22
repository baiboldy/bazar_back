from typing import List

from pydantic import BaseModel, Field, HttpUrl

class Image(BaseModel):
    imageUrl: HttpUrl
    name: str

class Category(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()
    images: List[Image] = Field()
