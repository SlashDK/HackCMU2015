import requests
import string

title = raw_input("What are you reading? ")

def searchForBook(title): #takes in user input, returns id for best match
    result = ""
    payload = {'q':title, 'key':'NsvXiH6QA7O1q3SvBLtvA'}
    r = requests.get('https://www.goodreads.com/search/index.xml', params=payload)
    r = str(r.text).splitlines()
    ID = r[r.index('  <best_book type="Book">') + 1]
    matchFound = ID = r[r.index('  <best_book type="Book">') + 2]
    matchFound = matchFound.split('>')
    matchFound = matchFound[1].split("<")
    matchFound = matchFound[0]
    for c in ID:
        if c.isdigit():
            result += c
    print("Search Result: %s" % matchFound)
    return result
    
    
def getGenres(): #given ID, returns XML containing genres for book
    genres = []
    payload = {'format':'xml', 'key':'NsvXiH6QA7O1q3SvBLtvA', 'id':searchForBook(title), 'text_only':'False'}
    r = requests.get("https://www.goodreads.com/book/show/50", params=payload)
    r = str(r.text).splitlines()
    for line in r:
        if line.startswith("      <shelf"):
            genres.append(line.split('"')[1])
    print(genres)


getGenres()
