from pymongo import MongoClient
import test
client=MongoClient(f"mongodb+srv://admin:{test}!@cluster0.70cv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.todo_db
#createes database

'''1. collection in MongoDB
A collection in MongoDB is similar to a table in relational databases'''
collection_name=db["todo_collection"]

