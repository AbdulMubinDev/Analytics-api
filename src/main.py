from fastapi import FastAPI
from api.events import router as event_router


app = FastAPI()
app.include_router(event_router, prefix="/api/events")



