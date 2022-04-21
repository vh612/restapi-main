import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#get list of database from MongoDB
print(myclient.list_database_names())