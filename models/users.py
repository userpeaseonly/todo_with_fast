from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "password",
                "events": [
                    {
                        "id": 1,
                        "title": "Event Title",
                        "image": "https://example.com/image.jpg",
                        "description": "Event Description",
                        "tags": ["tag1", "tag2"],
                        "location": "Event Location",
                    }
                ]
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
