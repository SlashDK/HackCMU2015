# ourapp/views.py
import Main
from flask import render_template, redirect, url_for, Flask, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
import requests
from forms import BookForm
Bootstrap(app)
@app.route('/index', methods=["GET", "POST"])
def index():
    form = BookForm(csrf_enabled=False)
    if form.validate_on_submit():
        # Check the password and log the user in
        # [...]
        artist=Main.main(form.book.data)
        print( artist)
        if(artist=="Hans Zimmer"):
            album_uri = "spotify:album:61xHE9mlaQK7Pn02Qr3Scy";
        elif(artist=="Steve Jablonsky"):
            album_uri="spotify:album:1TA5Qdd6dgt9vGw9JZqJDF"
        elif(artist=="Eluvium"):
            album_uri="spotify:album:4BMYwbOZd1i9vraiSXtSkg"
        elif(artist=="John Williams"):
            album_uri="spotify:album:7n26GKaWGJ1sx9CXKISyyE"
        elif(artist=="Kenny G"):
            album_uri="spotify:album:5ie513eFL7o8i9kesVzoNW"
        elif(artist=="Beethoven"):
            album_uri="spotify:album:5zhKcnv4IvJXZ8oj3TyYCH"
        print(album_uri)
        return render_template('index.html', form=album_uri)
    #print(form.validate_on_submit())
    return render_template('index.html')

@app.route('/qwerty', methods=["GET"])
def qwerty():
    return "Hello World"




# @app.route('/getspotify',methods=["GET"])
# def music():
#     print "music1"
#     art=request.args.get("q")
#     print "music2"
#     r = requests.get("http://ws.spotify.com/search/1/artist.json?q="+art)
#     print "music3"
#     return r

# @app.route('/getspotifyalbum',methods=["GET"])
# def music123():
#     artist_id=request.args.get("q")
#     r = requests.get('https://api.spotify.com/v1/artists/'+artist_id+'/albums')
#     return r
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')