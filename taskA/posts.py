import requests
import mongodb

#importing users table from database
usersTable = mongodb.db.Users

#function for handling request posts data from api
def fetch_posts(id):
  #fetch posts from API
  data = requests.get("https://dummyapi.io/data/v1/user/"+ str(id) +"/post", headers={'app-id': '6513ed5b2a8784116e313983'})
  #covert fetched data to json
  data = data.json()["data"]
  print(f"fetched posts data from dummy api for user {id}")
  return data

#function for populating data into database
def populate_posts(id, data):
  #try catch block to check handle if user is already present in database
  try:
    #inserting data into database
    print(f"**********populating user {id} with posts**************")
    usersTable.update_one({'_id':id},{"$set":{"posts": data}})
  except:
    print("User posts already present in dabase add new posts")