from select import select
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Request
from database.connection import get_session
from models.events import Event, EventUpdate

from beanie import PydanticObjectId
from database.connection import Database

event_router = APIRouter()

event_database = Database(Event)


@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {"message": "Event created successfully"}


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    events = await event_database.get_all()
    return events


# @event_router.get("/{event_id}", response_model=Event)
# async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
#     event = session.get(Event, id)
#     if event:
#         return event
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


@event_router.put("edit/{event_id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)):
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")


@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully."
    }
