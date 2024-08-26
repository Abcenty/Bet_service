from fastapi import FastAPI

import routing

app = FastAPI()

app.include_router(routing.events_router, prefix="", tags=["События"])