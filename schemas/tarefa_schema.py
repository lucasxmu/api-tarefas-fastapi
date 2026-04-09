from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prioridade: int
    concluida: bool