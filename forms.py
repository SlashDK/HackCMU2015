# ourapp/forms.py
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required, Email

class BookForm(Form):
    book = TextField('book', validators=[Required()])
    