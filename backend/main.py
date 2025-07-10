from fastapi import FastAPI
from api import simulate

app = FastAPI()
app.include_router(simulate.router)

