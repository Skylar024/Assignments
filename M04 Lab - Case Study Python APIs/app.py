from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String(80), unique=True, nullable=False)
    authorName = db.Column(db.String(80), unique=False, nullable=False)
    publisherName = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.bookName} - {self.authorName}"


@app.route('/')
def index():
    return "Hello!"

@app.route("/books")
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'id': book.id, 'bookName': book.bookName, 'authorName': book.authorName, 'publisherName': book.publisherName}
        
        output.append(book_data)
    
    return {'books': output}