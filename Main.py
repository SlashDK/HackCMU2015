import requests
import string

class mainGenre:
    def getGenreLink(self,baseGenre):
        #awe = Hans Zimmer
        #action = Steve Jablonsky
        #dark = Gyorgy Ligeti
        #sad = Eluvium
        #sci-fi = John Williams
        #romance = Kenny G
        #general = Beethoven
        genreLink={
'Hans Zimmer':['feminism','historical','biblical','fantasy', 'christian','inspirational', 'surreal', 'religion', 'theology'],
'Steve Jablonsky':['action','adventure', 'war', 'survival'],
'Gyorgy Ligeti':['dark', 'death','witchcraft','occult', 'dark-fantasy', 'horror'],
'Eluvium':[ 'disability','anthologies'],
'John Williams':['science-fiction', 'sci-fi','space', 'sci-fi-fantasy'], 
'Kenny G':['gender',  'holiday',  'love','relationships', 'romantic', 'social', 'womens', 'fifty-shades'],
'Beethoven':['animals', 'diary', 'management', 'medical', 'textbooks', 'wildlife','drama']
}
        genreKey=['Hans Zimmer','Steve Jablonsky','Gyorgy Ligeti','Eluvium','John Williams','Kenny G', 'Beethoven']
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
    r = r.text.encode('utf-8').splitlines()
    for line in r:
        if line.startswith("      <shelf"):
            genres.append(line.split('"')[1])
    return genres

def main():
    obj=mainGenre()
    genresList=getGenres()#link to genres list from api
    musician=None
    for c in genresList:
        musician=obj.getGenreLink(c)
        if(musician!=None):
            break
        if(musician==None):
            genre='general'
    #print(genresList)
    #Goes through list to assign main genre.
    #print (genre)
    #print(obj.genre)
    #print (obj.number) 
    print(musician)
    return musician

if __name__ == "__main__":
    main()
        