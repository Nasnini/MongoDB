from pymongo import MongoClient

connect('mongoengine_UmuziProspects', host='localhost', port=27017)
client = MongoClient("mongodb://root:rootpassword@localhost:27017")

db = client["pymongo_UmuziProspects"]
my_db = db["Visiter"]