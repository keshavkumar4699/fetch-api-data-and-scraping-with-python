import taskA.users as users
import taskA.posts as posts
import mongodb

def task():
  print("inside task of taskA")
  #******FOR FETCHING USERS DATA FROM API AND INSERTING IN DATABASE*******

  #fetch data from api
  user_data = users.fetch_users()

  #insert users data into database(if already present it will show duplication erro)
  users.insert_users(user_data)


  #******FOR POPULATING USERS WITH POSTS*******

  #importing users table from database
  usersTable = mongodb.db.Users

  #iterate over usersTable in database
  for user in usersTable.find():
    #get current user id from all users from database
    user_Id = user["_id"]

    #fetch posts of relevant users from API
    post_data = posts.fetch_posts(user_Id)

    #populate users in database with fetched posts
    posts.populate_posts(user_Id, post_data)