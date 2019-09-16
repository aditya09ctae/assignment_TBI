# this one is main class

from sqlalchemy import func, case

from DBLayer.DBConnection import Base, session_factory
from model.book import Book
from model.rating import Rating
from model.book_final import BookFinal


# Below function load book data to postgres
def create_books(db_type, input_file, bad_data_file):
    session = session_factory(db_type)
    print(session)
    loop_var = 0
    if input_file.mode == 'r':
        for book_data in input_file:
            print(loop_var)
            # ignore header row
            if loop_var == 0:
                loop_var = 1
                continue
            book_data_list = book_data.rstrip().replace('\n', '').replace('"', '').split(";")

            if len(book_data_list) == 8:
                try:
                    ISBN = book_data_list[0]
                    bookTitle = book_data_list[1]
                    bookAuthor = book_data_list[2]
                    yearOfPublication = int(book_data_list[3].replace('"', ''))
                    publisher = book_data_list[4]
                    imageURLS = book_data_list[5]
                    imageURLM = book_data_list[6]
                    imageURLL = book_data_list[7]
                    bookObj = Book(ISBN, bookTitle, bookAuthor, yearOfPublication, publisher, imageURLS, imageURLM,
                                   imageURLL)
                    session.add(bookObj)
                    session.commit()
                except:
                    # put data into bad_data_file
                    bad_data_file.write(book_data)
            else:
                bad_data_file.write(book_data)
            loop_var = loop_var + 1  # used for checking the execution
        loop_var = 0
    session.commit()
    session.close()


# load rating csv file to mysql
def create_ratings(db_type, input_file, bad_data_file):
    session = session_factory(db_type)
    loop_var = 0
    if input_file.mode == 'r':
        for book_rating in input_file:
            print(loop_var)
            # ignoring header row
            if loop_var == 0:
                loop_var = 1
                continue
            book_rating_list = book_rating.rstrip().replace('\n', '').replace('"', '').split(";")
            # print(len(book_rating_list))
            if len(book_rating_list) == 3:
                try:
                    # print("inside try")
                    userId = int(book_rating_list[0])
                    ISBN = book_rating_list[1]
                    rating = int(book_rating_list[2])
                    if len(ISBN) > 15:
                        raise ValueError('ISBN length is not 10')
                    ratingObj = Rating(userId, ISBN, rating)
                    session.add(ratingObj)
                    session.commit()
                except:
                    # put data into bad_data_file
                    bad_data_file.write(book_rating)
            else:
                bad_data_file.write(book_rating)
            loop_var = loop_var + 1
        loop_var = 0
    session.commit()
    session.close()


# get all books
def get_books(db_type):
    session = session_factory(db_type)
    books_query = session.query(Book)
    session.close()
    return books_query.all()


# get ratings of the book by isbn
def get_ratings_by_isbn(req_isbn, session):
    xpr0 = func.sum(case([(Rating.rating == 0, 1), ], else_=0)).label("countOfrating_0")
    xpr1 = func.sum(case([(Rating.rating == 1, 1), ], else_=0)).label("countOfrating_1")
    xpr2 = func.sum(case([(Rating.rating == 2, 1), ], else_=0)).label("countOfrating_2")
    xpr3 = func.sum(case([(Rating.rating == 3, 1), ], else_=0)).label("countOfrating_3")
    xpr4 = func.sum(case([(Rating.rating == 4, 1), ], else_=0)).label("countOfrating_4")
    xpr5 = func.sum(case([(Rating.rating == 5, 1), ], else_=0)).label("countOfrating_5")
    xpr6 = func.sum(case([(Rating.rating == 6, 1), ], else_=0)).label("countOfrating_6")
    xpr7 = func.sum(case([(Rating.rating == 7, 1), ], else_=0)).label("countOfrating_7")
    xpr8 = func.sum(case([(Rating.rating == 8, 1), ], else_=0)).label("countOfrating_8")
    xpr9 = func.sum(case([(Rating.rating == 9, 1), ], else_=0)).label("countOfrating_9")
    xpr10 = func.sum(case([(Rating.rating == 10, 1), ], else_=0)).label("countOfrating_10")

    books_query = session.query(Rating.ISBN, xpr0, xpr1, xpr2, xpr3, xpr4, xpr5, xpr6, xpr7, xpr8, xpr9, xpr10,
                                func.count(Rating.userId)).filter(Rating.ISBN == req_isbn).group_by(Rating.ISBN)
    return books_query.all()


# business logic to combine both the data
def combineBookAndRating(book, rating):
    ISBN = book.ISBN
    bookTitle = book.bookTitle
    bookAuthor = book.bookAuthor
    yearOfPublication = book.yearOfPublication
    publisher = book.publisher
    imageURLS = book.imageURLS
    imageURLM = book.imageURLM
    imageURLL = book.imageURLL
    numOfUsers = rating[12]
    countOfrating_0 = rating[1]
    countOfrating_1 = rating[2]
    countOfrating_2 = rating[3]
    countOfrating_3 = rating[4]
    countOfrating_4 = rating[5]
    countOfrating_5 = rating[6]
    countOfrating_6 = rating[7]
    countOfrating_7 = rating[8]
    countOfrating_8 = rating[9]
    countOfrating_9 = rating[10]
    countOfrating_10 = rating[11]
    book_final_obj = BookFinal(ISBN, bookTitle, bookAuthor, yearOfPublication, publisher, imageURLS, imageURLM,
                               imageURLL,
                               numOfUsers, countOfrating_0, countOfrating_1, countOfrating_2, countOfrating_3,
                               countOfrating_4,
                               countOfrating_5, countOfrating_6, countOfrating_7, countOfrating_8, countOfrating_9,
                               countOfrating_10)

    return book_final_obj


if __name__ == "__main__":

    db_type_for_book = 'postgres'
    book_file = open('input_files/BX-Books.csv', 'r', encoding='latin-1')
    bad_book_data_file = open('bad_data/bad_books_file.csv', 'w')
    create_books(db_type_for_book, book_file, bad_book_data_file)
    book_file.close();
    bad_book_data_file.close()

    db_type_for_rating = 'mysql'
    ratings_file = open('input_files/BX-Book-Ratings.csv', 'r', encoding='latin-1')
    bad_ratings_data_file = open('bad_data/bad_rating_file.csv', 'w')
    create_ratings(db_type_for_rating, ratings_file, bad_ratings_data_file)
    ratings_file.close();
    bad_ratings_data_file.close()

    books = get_books('postgres')
    session_postgres = session_factory('postgres')
    session_mysql = session_factory('mysql')
    loop_var = 0
    for book in books:
        print(loop_var)
        ratings = get_ratings_by_isbn(book.ISBN, session_mysql)
        for rating in ratings:
            final_book_obj = combineBookAndRating(book, rating)
            session_postgres.add(final_book_obj)
            session_postgres.commit()
        loop_var = loop_var + 1
    session_mysql.close()
    session_postgres.close()
