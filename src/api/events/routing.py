from fastapi import APIRouter
from .schemas import EventSchemas, EventListSchemas
router = APIRouter()


@router.get('/')
def read_event() -> EventListSchemas:
    return {
        'number': [{'id': 1}, {'id': 2}, {'id': 3}]
    }


@router.get('/{id}')
def get_event(id: int) -> EventSchemas:
    return {
        "id": id
    }