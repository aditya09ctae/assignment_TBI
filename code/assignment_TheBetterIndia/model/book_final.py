# Model for final - Combination of books with ratings

from sqlalchemy import Column, String, Date, Integer, Numeric
from DBLayer.DBConnection import Base


class BookFinal(Base):
    __tablename__ = 'book_details_final'

    id = Column(Integer, primary_key=True)
    ISBN = Column(String(15))
    bookTitle = Column(String(300))
    bookAuthor = Column(String(150))
    yearOfPublication = Column(Numeric)
    publisher = Column(String(150))
    imageURLS = Column(String(250))
    imageURLM = Column(String(250))
    imageURLL = Column(String(250))
    numOfUsers = Column(Numeric)
    countOfrating_0 = Column(Numeric)
    countOfrating_1 = Column(Numeric)
    countOfrating_2 = Column(Numeric)
    countOfrating_4 = Column(Numeric)
    countOfrating_5 = Column(Numeric)
    countOfrating_6 = Column(Numeric)
    countOfrating_7 = Column(Numeric)
    countOfrating_8 = Column(Numeric)
    countOfrating_9 = Column(Numeric)
    countOfrating_10 = Column(Numeric)


    def __init__(self, ISBN, bookTitle , bookAuthor , yearOfPublication, publisher, imageURLS , imageURLM, imageURLL,
                 numOfUsers, countOfrating_0 ,countOfrating_1 ,countOfrating_2 ,countOfrating_3 ,countOfrating_4 ,
                 countOfrating_5,countOfrating_6 ,countOfrating_7 ,countOfrating_8 ,countOfrating_9 ,countOfrating_10):
        self.ISBN = ISBN
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.yearOfPublication = yearOfPublication
        self.publisher = publisher
        self.imageURLS = imageURLS
        self.imageURLM = imageURLM
        self.imageURLL = imageURLL
        self.numOfUsers = numOfUsers
        self.countOfrating_0 = countOfrating_0
        self.countOfrating_1 = countOfrating_1
        self.countOfrating_2 = countOfrating_2
        self.countOfrating_3 = countOfrating_3
        self.countOfrating_4 = countOfrating_4
        self.countOfrating_5 = countOfrating_5
        self.countOfrating_6 = countOfrating_6
        self.countOfrating_7 = countOfrating_7
        self.countOfrating_8 = countOfrating_8
        self.countOfrating_9 = countOfrating_9
        self.countOfrating_10 = countOfrating_10
