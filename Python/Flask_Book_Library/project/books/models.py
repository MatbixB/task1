from project import db, app
import re
import html

# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer) 
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        if(len(name)<1 or len(name)>64):
            raise ValueError("Invalid length of name string")
        self.name = html.escape(name)
        if(len(author)<1 or len(author)>64):
            raise ValueError("Invalid length of author string")
        if not (re.match(r"^[\w\-\s]+$", author)):
            raise ValueError("Unexpected characters in author string")
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"


with app.app_context():
    db.create_all()