import xml.parsers.expat
class mainGenre:
    def getGenreLink(self,baseGenre):
        genreLink={
'awe':['feminism','historical','biblical','fantasy', 'christian','inspirational','space', 'surreal'],
'action':['action','adventure','war'],
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

def main():
    obj=mainGenre()
    genresList=["datshit"]#link to genres list from api
    genre=None
    for c in genresList:
        genre=obj.getGenreLink(c)
        if(genre!=None):
            break
        if(genre==None):
            genre='general'
    #Goes through list to assign main genre.
    #print (genre)
    #print(obj.genre)
    #print (obj.number) 

if __name__ == "__main__":
    main()
        