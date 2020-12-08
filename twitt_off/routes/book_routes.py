# these routes will prepare fetch data from the database
# and store data in the database
from flask import Blueprint, jsonify, request, render_template

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"}
    ]
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("books.html", messege="Here's some books", books=books)
# render_templates - special flask method to retun html file, 
# 1 - name of the file
# 2 - meassege
# 3 - data that we hope to inject into the page
# Pattern is the same as in the home routes

@book_routes.route("/books/new")
# renders our new book, which has on it a form
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
# sends a post request to /books/create
def create_book():
    # prints the data that gets send 
    print("FORM DATA", dict(request.form))
    # todo: store in database
    # says what to with that data
    return jsonify({
        "messege": "BOOK CREATED OK (TODO)", 
        "book": dict(request.form)
    })
