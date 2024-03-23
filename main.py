from fastapi import FastAPI
from database import Base, engine
from machine.machine_api import machine_router


app = FastAPI(docs_url='/')
app.include_router(machine_router)

Base.metadata.create_all(bind=engine)