import requests
from bs4 import BeautifulSoup

#function to scrape books from website and return all books in a dictionary
def return_scrape_data() -> list:

  #dictionary for storing all scraped books
  allBooks = []

  #to count how many books has been accessed
  bookCount = 0

  # Since the url-> https://books.toscrape.com have 50 pages 1-50, so iterating from [1, 51)(51 not included) 
  for i in range(1, 51):
    #pring the currently accessed page
    print(f"accessing page {i} for books")

    #url of scraping website
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    #request variable of url
    r = requests.get(url)

    # saving html file in homePage variable as text data
    htmlPage = r.text

    #parse html page using the beautiful soup library to scrape data easily using this library
    soup = BeautifulSoup(htmlPage, 'html.parser')

    #accessing html tag list having book content
    books = soup.find("section").find(class_ = "row").find_all("li")
    
    # Iterating over every book found on this page
    for book in books:
      bookDictionary = dict()

      # Fetching book data

      img_url = book.find("img").get("src")
      # class has two attributes: "star-rating" and rating eg."Three" so selecting 1st element.(0 based indexing)
      rating = book.find("p").get("class")[1]
      title = book.find("h3").find("a").get("title")
      price = book.find(class_ = "product_price").find(class_ = "price_color").text.strip()
      # omitting special character
      price = price[1:]
      availability = book.find(class_ = "availability").text.strip()

      # creating keys in dictionary for above fetched data
      bookDictionary["image_url"] = "https://books.toscrape.com" + img_url[2:]
      bookDictionary["rating"] = rating
      bookDictionary["title"] = title
      bookDictionary["price"] = price
      bookDictionary["availability"] = availability

      #printing current book
      bookCount+=1
      print(f"fetching book no: {bookCount}")

      #putting current book in all book dictionary
      allBooks.append(bookDictionary)
  
  return allBooks