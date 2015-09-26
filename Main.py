import requests
import string

class mainGenre:
    def getGenreLink(self,baseGenre):
        genreLink={
'awe':['feminism','historical','biblical','fantasy', 'christian','inspirational','space', 'surreal', 'religion', 'theology'],
'action':['action','adventure', 'war'],
'dark':['dark', 'death','witchcraft','occult'],
'sad':[ 'disability','anthologies'],
'romance':['gender',  'holiday',  'love','relationships', 'romantic', 'social', 'womens'],
'general':['animals', 'diary', 'management', 'medical', 'textbooks', 'wildlife','drama']
}
        genreKey=['awe','action','dark','sad','romance','general']
        for c in genreKey:
            if baseGenre in genreLink[c]:
                #print(c)
                return c
        return None

title = raw_input("What are you reading? ")

def searchForBook(title): #takes in user input, returns id for best match
    result = ""
    payload = {'q':title, 'key':'NsvXiH6QA7O1q3SvBLtvA'}
    r = requests.get('https://www.goodreads.com/search/index.xml', params=payload)
    r = str(r.text).splitlines()
    ID = r[r.index('  <best_book type="Book">') + 1]
    matchFound = r[r.index('  <best_book type="Book">') + 2]
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
    r = requests.get("https://www.goodreads.com/book/show/", params=payload)
    r = str(r.text).splitlines()
    for line in r:
        if line.startswith("      <shelf"):
            genres.append(line.split('"')[1])
    return genres

def main():
    obj=mainGenre()
    genresList=getGenres()#link to genres list from api
    genre=None
    for c in genresList:
        genre=obj.getGenreLink(c)
        if(genre!=None):
            break
        if(genre==None):
            genre='general'
    print(genresList)
    #Goes through list to assign main genre.
    #print (genre)
    #print(obj.genre)
    #print (obj.number) 
    print(genre)

if __name__ == "__main__":
    main()
        