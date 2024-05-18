from beanie import Document
from typing import Optional, List


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Event Title",
                "image": "https://example.com/image.jpg",
                "description": "Event Description",
                "tags": ["tag1", "tag2"],
                "location": "Event Location",
            }
        }

    class Settings:
        name = "events"


class EventUpdate(Document):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Event Title",
                "image": "https://example.com/image.jpg",
                "description": "Event Description",
                "tags": ["tag1", "tag2"],
                "location": "Event Location",
            }
        }
