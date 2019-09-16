# model for book

from sqlalchemy import Column, String, Integer, Numeric
from DBLayer.DBConnection import Base


class Book(Base):
    __tablename__ = 'book_details'
    id = Column(Integer, primary_key=True)
    ISBN = Column(String(15))
    bookTitle = Column(String(300))
    bookAuthor = Column(String(150))
    yearOfPublication = Column(Numeric)
    publisher = Column(String(150))
    imageURLS = Column(String(250))
    imageURLM = Column(String(250))
    imageURLL = Column(String(250))

    def __init__(self, ISBN, bookTitle, bookAuthor, yearOfPublication, publisher, imageURLS, imageURLM, imageURLL):
        self.ISBN = ISBN
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.yearOfPublication = yearOfPublication
        self.publisher = publisher
        self.imageURLS = imageURLS
        self.imageURLM = imageURLM
        self.imageURLL = imageURLL
