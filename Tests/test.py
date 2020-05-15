from PyUmuziProspects import *
import unittest
from mongo_engine_code import *

class test_mongo(unittest.TestCase):
    
    # Test if the Visitor is saved into the collection
    def test_Create_Visitor(self):
        assert create_visitor

    # Test should return an array of all the visitor names and ids
    def test_List_Visitor(self):
        assert list_visitor

    # Test if the visitor is successfully deleted
    def test_Delete_Visitor(self):
        assert delete_visitor

    # Test if only a single documnet is updated in the collection
    def test_Update_Visitor(self):
        assert update_visitor

    # Test if ID returns information about the visitor
    def test_Visitor_Details(self):
        assert visitor_details

    # Test if all the collections are deleted
    def test_Delete_All(self):
        assert delete_all