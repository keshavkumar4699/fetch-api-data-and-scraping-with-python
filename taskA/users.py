import requests
from bson import ObjectId
import mongodb

#importing userstable from database
usersTable = mongodb.db.Users

#function for handling users request data from api
def fetch_users():
  # fetch users from API 
  data = requests.get("https://dummyapi.io/data/v1/user", headers={'app-id': '6513ed5b2a8784116e313983'})
  #convert fetched data to json
  data = data.json()["data"] 
  print("fetched users data from dummy api")
  return data

#function for inserting data into database
def insert_users(data):
  #converting ids of object from string to ObjectIds for storage
  for i in data:
    i["_id"]=i.pop("id")
    oid_str=i["_id"]
    i["_id"]=ObjectId(oid_str)

  #try catch block to check handle if post is already present in database
  try:
    #inserting data into database
    usersTable.insert_many(data)
    print("fetched data from dummy api is inserted into database")
  except:
    print("Data already present in database add new User")