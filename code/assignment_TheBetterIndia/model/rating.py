#model for rating

from sqlalchemy import Column, String, Date, Integer, Numeric
from DBLayer.DBConnection import Base


class Rating(Base):
    __tablename__ = 'book_ratings'
    id = Column(Integer, primary_key=True)
    userId = Column(Numeric)
    ISBN = Column(String(15))
    rating = Column(Numeric)

    def __init__(self, userId, ISBN, rating):
        self.userId = userId
        self.ISBN = ISBN
        self.rating = rating
