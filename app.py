# ourapp/views.py
import Main
from flask import render_template, redirect, url_for, Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
from forms import BookForm
Bootstrap(app)
@app.route('/index', methods=["GET", "POST"])
def index():
    form = BookForm(csrf_enabled=False)
    if form.validate_on_submit():
        # Check the password and log the user in
        # [...]
        artist=Main.main(form.book.data)
        return redirect(url_for('index'))
        return redirect(url_for('qwerty'))
    return render_template('index.html', form=form)

@app.route('/qwerty', methods=["GET", "POST"])
def qwerty():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')