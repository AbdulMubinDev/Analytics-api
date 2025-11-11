from pydantic import BaseModel
from typing import List


class EventSchemas(BaseModel):
    id: int
    
    
    
class EventListSchemas(BaseModel):
    number: List[EventSchemas]