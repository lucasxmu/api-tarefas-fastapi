from fastapi import FastAPI
from routers.tarefa_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Tarefas com FastAPI + MongoDB + Docker"}