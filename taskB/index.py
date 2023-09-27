import mongodb
import taskB.scrapebook as scrapebook

def task():
  #importing books table from database
  booksTable = mongodb.db.Books

  #get scrape books data
  allBooks = scrapebook.return_scrape_data()

  try:
    #inserting books data into database
    booksTable.insert_many(allBooks)
    print("$$$$$$ ALL BOOKS ARE IN DATABASE $$$$$$")
  except:
    print("Error in putting data into database")