from pymongo import MongoClient
import pymongo
from mongoengine import *

# Connection String to the database - ****Makes these environmnetal variables
connect('mongoengine_UmuziProspects', host='localhost', port=27017)
client = MongoClient("mongodb://root:rootpassword@localhost:27017")

# Instance of the connection to the database and collection
db = client["UmuziProspects"]
my_db = db["Visiter"]

my_query_dict = [
    {id: "", visitors_name: "Nasni", visitors_age: "25", date_of_visit: "2020-03-26", time_of_visit: "12:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"}
    {id: "", visitors_name: "Matt", visitors_age: "36", date_of_visit: "2020-01-19", time_of_visit: "14:36", assisted_by: "Nthombi Brown", comments: "student at Umuzi"}
    {id: "", visitors_name: "John", visitors_age: "48", date_of_visit: "2019-12-08", time_of_visit: "10:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"}
    {id: "", visitors_name: "Nasni", visitors_age: "25", date_of_visit: "2020-03-26", time_of_visit: "12:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"}
    {id: "", visitors_name: "Nasni", visitors_age: "25", date_of_visit: "2020-03-26", time_of_visit: "12:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"}
]

# create_visitor - Should save the visitor into the database/collection 
def create_visitor():
    my_db.Visiter.insert({id: "", visitors_name: "Nasni", visitors_age: "25", date_of_visit: "2020-03-26", time_of_visit: "12:30", assisted_by: "Nthombi Brown", comments: "student at Umuzi"})
    my_db.Visiter.insert({id: "", visitors_name: "Tshepo", visitors_age: "30", date_of_visit: "2020-05-30", time_of_visit: "14:40", assisted_by: "Siphokazi Mjali", comments: "Lecturer"})
    

# list_visitors - returns an array of visitors_name: and ObjectId
def list_visitors():
    visitor_list = my_db.find_one()
    return visitor_list


# delete_visitor - Deletes a single document from the collection
def delete_visitor():
    my_query_dict = {"visitor_name": "John"}
    my_db.deleteOne(my_query_dict)


# update_visitor - Update a single document in the collection
def update_visitor():
    new_values = { "$set": }


# visitor_details - Using the visitor's ID - returns all information about that visitor
def visitor_details():
    visitor_info = my_db.find(my_query_list)

    for x in visitor_info:
        print(x)


# delete_all -Deletes documents from the collection
def delete_all():
    delete_visitors = my_db.delete_many({})
    print(delete_visitors, "documents in collection deleted.")