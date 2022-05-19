from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/IF"
    client = MongoClient(CONNECTION_STRING)
    return client


def insert_data(mongo_client, data: dict):
    db = mongo_client['db']
    col = db["artifacts"]
    col.insert_one(data)


def find_data(mongo_client, id):
    db = mongo_client['db']
    col = db["artifacts"]
    return col.find_one({"id": id},)


def get_lines(mongo_client):
    db = mongo_client['db']
    col = db["artifacts"]
    all_data = list(col.find({}))
    return [i["data"] for i in all_data]


def del_all(mongo_client):
    db = mongo_client['db']
    col = db["artifacts"]
    col.delete_many({})


