from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String,Integer,Float
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

all_books = []
@app.route('/')
def home():
    return render_template("index.html",books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        new_book=Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        # all_books.append(new_book)  # rather we are updating in the database
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True,port=5001)


# _______________********* Start of SQLite ***********________________
# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor=db.cursor()
# cursor.execute(
#     "CREATE TABLE books("
#     "id INTEGER PRIMARY KEY, "
#     "title varchar(250) NOT NULL UNIQUE, "
#     "author varchar(250) NOT NULL, "
#     "rating FLOAT NOT NULL)"
#                )
# cursor.execute("INSERT INTO books VALUES(2, 'Harry 1 Potter', 'J. K. Rowling', '9.3')")
# db.commit()







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







# # ___________**********Sql alchemy *************________________
#
# class Base(DeclarativeBase):
#   pass
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# db = SQLAlchemy(model_class=Base)
#
# db.init_app(app) # initialize the db for the app
#
# # table schema
# class Book(db.Model):
#     id: Mapped[int] = mapped_column(Integer,primary_key=True)
#     title:Mapped[str]=mapped_column(String(250),unique=True,nullable=False)
#     author:Mapped[str]=mapped_column(String(250),nullable=False)
#     rating:Mapped[float]=mapped_column(Float,nullable=False)
#
# # creates the table schema
# with app.app_context():
#     # object call
#     db.create_all()
#
# # CREATE RECORD CRUD
# # When creating new records, the primary key fields is optional. you can also write:
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
#
# # read all records CRUD
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_book = result.scalars()
#
# # read single record CRUD, use scalar instead of scalars
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#
# #Update a particular record CRUD,
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# # update a record by primary key, CRUD
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# # for get method in CRUD- get_or_404()
# # Delete a particular record from database
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

