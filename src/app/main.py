"""endpoint for an app example bellow"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#example for router:
"""
from routers import plant
app.include_router(plant.router)
"""