from fastapi import FastAPI

import routing

app = FastAPI()

app.include_router(routing.bets_router, prefix="/bets", tags=["Ставки"])
app.include_router(routing.events_router, prefix="/events", tags=["События"])