from typing import List

from pydantic import BaseModel


# class Item(BaseModel):
#     item: str
#     status: str
#
#
class Todo(BaseModel):
    id: int
    item: str


# class Todo(BaseModel):
#     id: int
#     item: str
#
#     class Config:
#         scheme_extra = {
#             "example": {
#                 "id": 1,
#                 "item": "Buy groceries"
#             }
#         }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Buy groceries"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Buy groceries"},
                    {"item": "Pay bills"}
                ]
            }
        }
