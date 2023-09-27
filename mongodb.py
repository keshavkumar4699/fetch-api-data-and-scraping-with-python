import pymongo

#connecting to database
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db=client['dummy']