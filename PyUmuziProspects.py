from pymongo import MongoClient

connect('mongoengine_UmuziProspects', host='localhost', port=27017)
client = MongoClient("mongodb://root:rootpassword@localhost:27017")

db = client["pymongo_UmuziProspects"]
my_db = db["Visiter"]

db.Visiter.insert({id: "", visitors_name: "Nasni", visitors_age: "25", date_of_visit: "2020-03-26", time_of_visit: "12:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"})

# create_visitor
def create_visitor():
    pass

# list_visitors
def list_visitors(self, parameter_list):
    pass

# delete_visitor
def delete_visitor():
    pass

# update_visitor
def update_visitor():
    pass

# visitor_details
def visitor_details():
    pass

# delete_all
def delete_all():
    pass
