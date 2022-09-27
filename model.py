import sqlalchemy as sq
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name_publisher = sq.Column(sq.String)

    def __repr__(self):
        return f"Автор: {self.name_publisher}, номер: {self.id_publisher}"


class Book(Base):
    __tablename__ = "book"
    id_book = sq.Column(sq.Integer, primary_key=True)
    book_title = sq.Column(sq.String(length=100), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id_publisher'))
    publisher = relationship("Publisher", backref='book')
    stocks = relationship("Stock", back_populates="book")

    def __repr__(self):
        return f"Название книги: {self.book_title}, автора: {self.id_publisher}"


class Shop(Base):
    __tablename__ = 'shop'
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), unique=True)
    stocks = relationship("Stock", back_populates="shop")

    def __repr__(self):
        return f"Shop(id={self.id_shop}, name={self.name})"


class Stock(Base):
    __tablename__ = 'stock'
    id_stock = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id_shop"), nullable=False)
    book = relationship("Book", back_populates="stocks")
    shop = relationship("Shop", back_populates="stocks")


class Sale(Base):
    __tablename__ = 'sale'
    id_sale = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    price = sq.Column(sq.Integer, nullable=False)
    data_sale = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id_stock"), nullable=False)
    stock = relationship("Stock", backref="stock")

def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

