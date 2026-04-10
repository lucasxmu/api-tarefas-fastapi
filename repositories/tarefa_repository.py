from database import tarefas_collection
from bson import ObjectId
from bson.objectid import InvalidId 


def create_tarefa(tarefa_dict):
    result = tarefas_collection.insert_one(tarefa_dict)
    return {"id": str(result.inserted_id)}

def get_all_tarefas():
    tarefas = list(tarefas_collection.find())
    for tarefa in tarefas:
        tarefa["_id"] = str(tarefa["_id"])
    return tarefas

def get_tarefa_by_id(tarefa_id):
    try:
        tarefa = tarefas_collection.find_one({"_id": ObjectId(tarefa_id)})
        if tarefa:
            tarefa["_id"] = str(tarefa["_id"])
        return tarefa
    except InvalidId:
        return {"error": "ID inválido"}

def update_tarefa(tarefa_id, tarefa_dict):
    try:
        obj_id = ObjectId(tarefa_id)  
    except InvalidId:
        return {"error": "ID inválido"}

    result = tarefas_collection.update_one(
        {"_id": obj_id},
        {"$set": tarefa_dict}
    )

    if result.matched_count == 0:  
        return {"error": "Tarefa não encontrada"}

    return {"message": "Tarefa atualizada com sucesso"}



def delete_tarefa(tarefa_id):
    try:
        result = tarefas_collection.delete_one(
            {"_id": ObjectId(tarefa_id)}
        )

        if result.deleted_count == 1:
            return {"message": "Tarefa deletada com sucesso"}
        else:
            return {"message": "Tarefa não encontrada"}

    except Exception as e:
        return {"error": str(e)}