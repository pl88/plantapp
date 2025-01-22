from fastapi import FastAPI

from routers import plant

app = FastAPI()

app.include_router(plant.router)

@app.get("/")
def get_root():
    return {"message": "Hello message"}

