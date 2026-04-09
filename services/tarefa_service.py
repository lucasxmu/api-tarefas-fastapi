from repositories.tarefa_repository import *

def create_tarefa_service(tarefa):
    return create_tarefa(tarefa.dict())

def get_all_tarefas_service():
    return get_all_tarefas()

def get_tarefa_by_id_service(tarefa_id):
    return get_tarefa_by_id(tarefa_id)

def update_tarefa_service(tarefa_id, tarefa):
    return update_tarefa(tarefa_id, tarefa.dict())

def delete_tarefa_service(tarefa_id):
    return delete_tarefa(tarefa_id)