from flask import Flask, render_template, json, redirect, url_for
from flask import request
import database.db_connector as db
import os

from logging import FileHandler,WARNING


file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app = Flask(__name__)

# Routes 

@app.route('/')
def index():
    return render_template("home.html")

def update_bna():
    '''Updates the books_and_authors junction table'''
    db_connection = db.connect_to_database()

    bna_query = "INSERT IGNORE INTO books_and_authors(books_book_id, author_author_id) \
        SELECT books.book_id, authors.author_id \
            FROM books, authors WHERE books.book_author_fname=authors.author_first_name \
                AND books.book_author_lname=authors.author_last_name"
    db.execute_query(db_connection, bna_query)

#----------------------#
#------SUBSCRIBERS-----#
#----------------------#

@app.route('/subscribers/')
def display_sub():
    db_connection = db.connect_to_database()
    query = "SELECT * from subscribers;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    return render_template("subscribers.html", subscribers=results)

@app.route('/subscribers_add/', methods = ['POST'])
def add_sub():
    db_connection = db.connect_to_database()
    first_name = request.form['fname']
    last_name = request.form['lname']
    address = request.form['address']
    phone = request.form['phone']

    query = "INSERT INTO subscribers(subscriber_first_name, subscriber_last_name, subscriber_address, subscriber_phone) VALUES(%s, %s, %s, %s);"
    sub_data = (first_name, last_name, address, phone)
    db.execute_query(db_connection, query, sub_data)
    return redirect(url_for('display_sub'))

@app.route('/subscribers_edit/<sid>', methods = ['GET', 'POST'])
def edit_sub(sid):
    db_connection = db.connect_to_database()
    first_name = request.form['fname']
    last_name = request.form['lname']
    address = request.form['address']
    phone = request.form['phone']

    query = "UPDATE subscribers SET subscriber_first_name = %s, subscriber_last_name = %s, subscriber_address = %s, subscriber_phone = %s WHERE subscriber_id = %s"
    new_data = (first_name, last_name, address, phone, sid)
    db.execute_query(db_connection, query, new_data)
    return redirect(url_for('display_sub'))

@app.route('/subscribers_delete/<sid>', methods = ['POST'])
def del_sub(sid):
    db_connection = db.connect_to_database()
    query = "DELETE FROM subscribers WHERE subscriber_id=%s" %(sid)
    db.execute_query(db_connection, query)
    return redirect(url_for('display_sub'))

@app.route('/subscribers_search/', methods = ['POST'])
def search_sub():
    db_connection = db.connect_to_database()
    keyword = request.form['search']
    print(keyword)
    query = "SELECT * FROM subscribers WHERE subscriber_first_name=%s OR subscriber_last_name=%s OR subscriber_address=%s OR subscriber_phone=%s"
    data = (keyword, keyword, keyword, keyword)
    results = db.execute_query(db_connection, query, data).fetchall()
    return render_template("subscribers.html", subscribers=results)

#----------------------#
#-------RENTALS--------#
#----------------------#

def get_SID():
    db_connection = db.connect_to_database()
    query = "SELECT subscriber_id from subscribers;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    return results

@app.route('/rentals/')
def display_rent():
    db_connection = db.connect_to_database()
    query = "SELECT * from rentals;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    sub_id = get_SID()
    return render_template("rentals.html", rentals=results, sids=sub_id)

@app.route('/rentals_add/', methods = ['POST'])
def add_rent():
    db_connection = db.connect_to_database()
    rental_date = request.form['rentalDate']
    rental_length = request.form['rentalLength']
    sid = request.form['rental_sids']

    query = "INSERT INTO rentals(rental_date, rental_length, subscriber_id) VALUES(%s, %s, (SELECT subscriber_id FROM subscribers WHERE subscriber_id=%s));"
    rent_data = (rental_date, rental_length, sid)
    db.execute_query(db_connection, query, rent_data)
    return redirect(url_for('display_rent'))

@app.route('/rentals_edit/<rid>', methods = ['GET', 'POST'])
def edit_rent(rid):
    db_connection = db.connect_to_database()
    rental_date = request.form['rentalDate']
    rental_length = request.form['rentalLength']
    sid = request.form['rental_sids']

    query = "UPDATE rentals SET rental_date = %s, rental_length = %s, subscriber_id = %s WHERE rental_id  = %s"
    new_data = (rental_date, rental_length, sid, rid)
    db.execute_query(db_connection, query, new_data)
    return redirect(url_for('display_rent'))

@app.route('/rentals_delete/<rid>', methods = ['POST'])
def del_rent(rid):
    db_connection = db.connect_to_database()
    query = "DELETE FROM rentals WHERE rental_id=%s" %(rid)
    db.execute_query(db_connection, query)
    return redirect(url_for('display_rent'))

@app.route('/rentals_search/', methods = ['POST'])
def search_rent():
    db_connection = db.connect_to_database()
    keyword = request.form['search']
    print(keyword)
    query = "SELECT * FROM rentals WHERE rental_date=%s OR rental_length=%s OR subscriber_id=%s"
    data = (keyword, keyword, keyword)
    results = db.execute_query(db_connection, query, data).fetchall()
    return render_template("rentals.html", rentals=results)

#----------------------#
#-------AUTHORS--------#
#----------------------#

@app.route('/authors/')
def display_auth():
    db_connection = db.connect_to_database()
    query = "SELECT * from authors;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    return render_template("authors.html", authors=results)

@app.route('/authors_add/', methods = ['POST'])
def add_auth():
    db_connection = db.connect_to_database()
    first_name = request.form['fname']
    last_name = request.form['lname']

    query = "INSERT INTO authors(author_first_name, author_last_name) VALUES(%s, %s);"
    auth_data = (first_name, last_name)
    db.execute_query(db_connection, query, auth_data)

    update_bna()

    return redirect(url_for('display_auth'))

@app.route('/authors_edit/<aid>', methods = ['GET', 'POST'])
def edit_auth(aid):
    db_connection = db.connect_to_database()
    first_name = request.form['fname']
    last_name = request.form['lname']

    query = "UPDATE authors SET author_first_name = %s, author_last_name = %s WHERE author_id = %s"
    new_data = (first_name, last_name, aid)
    db.execute_query(db_connection, query, new_data)
    return redirect(url_for('display_auth'))

@app.route('/authors_delete/<aid>', methods = ['POST'])
def del_auth(aid):
    db_connection = db.connect_to_database()
    query = "DELETE FROM authors WHERE author_id=%s" %(aid)
    db.execute_query(db_connection, query)
    return redirect(url_for('display_auth'))

@app.route('/authors_search/', methods = ['POST'])
def search_auth():
    db_connection = db.connect_to_database()
    keyword = request.form['search']
    query = "SELECT * FROM authors WHERE author_first_name=%s OR author_last_name=%s"
    data = (keyword, keyword)
    results = db.execute_query(db_connection, query, data).fetchall()
    return render_template("authors.html", authors=results)


#----------------------#
#---------BOOKS--------#
#----------------------#
def get_RID():
    db_connection = db.connect_to_database()
    query = "SELECT rental_id from rentals;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    return results

@app.route('/books/')
def display_books():
    db_connection = db.connect_to_database()
    query = "SELECT * from books;"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()
    rent_id = get_RID()
    return render_template("books.html", books=results, rids=rent_id)

@app.route('/books_add/', methods = ['POST'])
def add_books():
    db_connection = db.connect_to_database()
    name = request.form['name']
    pages = request.form['pages']
    year = request.form['year']
    publisher = request.form['publisher']
    genre = request.form['genre']
    auth_fname = request.form['authorFname']
    auth_lname = request.form['authorLname']
    rid = request.form['book_rids']

    query = "INSERT INTO books(book_name, book_pages, book_year, book_publisher, book_genre, book_author_fname, book_author_lname, rental_id) \
         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

    books_data = (name, pages, year, publisher, genre, auth_fname, auth_lname, rid)
    db.execute_query(db_connection, query, books_data)

    update_bna()

    return redirect(url_for('display_books'))

@app.route('/books_edit/<bid>', methods = ['GET', 'POST'])
def edit_books(bid):
    db_connection = db.connect_to_database()
    name = request.form['name']
    pages = request.form['pages']
    year = request.form['year']
    publisher = request.form['publisher']
    genre = request.form['genre']
    auth_fname = request.form['authorFname']
    auth_lname = request.form['authorLname']
    rid = request.form['book_rids']

    query = "UPDATE books SET book_name = %s, book_pages = %s, book_year = %s, book_publisher = %s, book_genre = %s, \
        book_author_fname = %s, book_author_lname = %s, rental_id = %s WHERE book_id = %s;"
    new_data = (name, pages, year, publisher, genre, auth_fname, auth_lname, rid, bid)
    db.execute_query(db_connection, query, new_data)
    return redirect(url_for('display_books'))

@app.route('/books_delete/<bid>', methods = ['POST'])
def del_books(bid):
    db_connection = db.connect_to_database()
    query = "DELETE FROM books WHERE book_id=%s" %(bid)
    db.execute_query(db_connection, query)
    return redirect(url_for('display_books'))

@app.route('/books_search/', methods = ['POST'])
def search_books():
    db_connection = db.connect_to_database()
    keyword = request.form['search']
    query = "SELECT * FROM books WHERE book_name = %s OR book_pages = %s OR book_year = %s OR book_publisher = %s \
        OR book_genre = %s OR book_author_fname = %s OR book_author_lname = %s OR rental_id = %s;"
    data = (keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword)
    results = db.execute_query(db_connection, query, data).fetchall()
    return render_template("books.html", books=results)

#----------------------#
#---BOOKS AND AUTHORS--#
#----------------------#

@app.route('/books_and_authors/')
def display_bna():
    
    db_connection = db.connect_to_database()

    query = "SELECT * FROM books_and_authors"
    cur = db.execute_query(db_connection=db_connection, query=query)
    results = cur.fetchall()

    return render_template("books_and_authors.html", bnas=results)
    
@app.route('/bna_search/', methods = ['POST'])
def search_bna():
    db_connection = db.connect_to_database()
    keyword = request.form['search']
    query = "SELECT * FROM books_and_authors WHERE books_book_id = %s OR author_author_id = %s;"
    data = (keyword, keyword)
    results = db.execute_query(db_connection, query, data).fetchall()
    return render_template("books_and_authors.html", bna=results)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3957)) 
    db_connection = db.connect_to_database()
    app.run(port=port, debug=True) 
