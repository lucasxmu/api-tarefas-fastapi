from database import tarefas_collection
from bson import ObjectId

def create_tarefa(tarefa_dict):
    result = tarefas_collection.insert_one(tarefa_dict)
    return {"id": str(result.inserted_id)}

def get_all_tarefas():
    tarefas = list(tarefas_collection.find())
    for tarefa in tarefas:
        tarefa["_id"] = str(tarefa["_id"])
    return tarefas

def get_tarefa_by_id(tarefa_id):
    tarefa = tarefas_collection.find_one({"_id": ObjectId(tarefa_id)})
    if tarefa:
        tarefa["_id"] = str(tarefa["_id"])
    return tarefa

def update_tarefa(tarefa_id, tarefa_dict):
    return tarefas_collection.update_one(
        {"_id": ObjectId(tarefa_id)},
        {"$set": tarefa_dict}
    )


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