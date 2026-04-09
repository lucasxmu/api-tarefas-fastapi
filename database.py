from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

db = client["meubanco"]
tarefas_collection = db["tarefas"]