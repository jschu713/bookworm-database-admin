-- CREATE functions; all values will be user input denoted by a colon (:) and suffix "Input"

-- Adding new subscriber
insert into subscribers(subscriber_first_name, subscriber_last_name, subscriber_address, subscriber_phone) 
	values(:subscriber_first_nameInput, :subscriber_last_nameInput, :subscriber_addressInput, :subscriber_phoneInput);

-- Adding new author
insert into authors(author_id, author_first_name, author_last_name) 
	values (:author_idInput, :author_first_nameInput, :author_last_nameInput);

-- Adding new book
insert into books(book_id, book_name, book_pages, book_year, book_publisher, book_genre) 
	values (:book_idInput, :book_nameInput, :book_pagesInput, :book_yearInput, :book_publisherInput, :book_genreInput);

-- Adding new rental
insert into rentals(rental_id, rental_date, rental_length, subscriber_id) 
	values (:rental_idInput, :rental_dateInput, :rental_lengthInput, :subscriber_idInput);

-- Adding books and authors
insert into books_and_authors(books_books__id, author_author_id)
	values (:books_books__idInput, :author_author_idInput;
    
-- READ functions

-- SELECT functions
-- SELECT all items in tables (useful for displaying all data upon user visiting corresponding page)

-- Subscriber page
select * from subscribers;

-- Author page
select * from authors;

-- Book page
select * from books;

-- Rental page
select * from rentals;

-- Books and authors page
select * from rentals;

-- SELECT item based on unique Primary Key, used in searching and displaying data; user variables denoted by colon and suffix "Input"

-- Subscriber page 
select * from subscribers 
	where subscriber_id=:subscriber_idInput;

-- Author page
select * from authors 
	where author_id=:author_idInput;

-- Book page 
select * from books 
	where book_id=:book_idInput;

-- Rental page
select * from rentals 
	where rental_id=:rental_idInput;

-- Books and authors page
select * from books_and_authors
	where books_books_id=:books_books_idInput;
    
-- UPDATE functions
-- UPDATE item based on unique Primary Key; user variables denoted by colon and suffix "Input"; any combination of listed variables may be updated

-- Subscriber page
update subscribers 
	set :subscriber_first_nameInput, :subscriber_last_nameInput, :subscriber_addressInput, :subscriber_phoneInput
    where 
    subscriber_id=:subscriber_idInput;

-- Author page
update authors
	set :author_first_nameInput, :author_last_nameInput
    where 
    author_id=:author_idInput;
    
-- Book page 
update books
	set :book_nameInput, :book_pagesInput, :book_yearInput, :book_publisherInput, :book_genreInput
	where 
    book_id=book_idInput;
    
-- Rental page
update rentals 
	set :rental_dateInput, :rental_lengthInput, :subscriber_idInput
    where 
	rental_id=:rental_idInput;
    
-- Books and authors page
update books_and_authors
	set :books_books_idInput, :author_authorInput
    where
    :books_books_id=:books_books_idInput;
    
-- DELETE functions
-- Deletes items based on unique Primary Key; user variables denoted by colon and suffix ''Input''

-- Subscribers
delete from subscribers where subscriber_id=:subscriber_idInput;

-- Authors
delete from authors where author_id=:author_idInput;

-- Books
delete from books where book_id=:book_idInput;

-- Rentals
delete from rentals where rental_id=:rental_idInput;

-- Books and authors
delete from books_and_authors where books_books_id=:books_books_idInput;
