import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from utilities import find_shop
from model import Publisher, Book, Shop, Stock, create_table

DSN = "postgresql://postgres:5240@localhost:5432/client"
engine = sq.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Publisher(name_publisher="Author_1")
author2 = Publisher(name_publisher="Author_2")
author3 = Publisher(name_publisher="Author_3")

book_1_author1 = Book(book_title="Первая книга автора 1", publisher=author1)
book_2_author1 = Book(book_title="Первая книга автора 1", publisher=author1)

book_1_author2 = Book(book_title="Первая книга автора 2", publisher=author2)
book_2_author2 = Book(book_title="Первая книга автора 2", publisher=author2)

book_1_author3 = Book(book_title="Первая книга автора 3", publisher=author3)
book_2_author3 = Book(book_title="Первая книга автора 3", publisher=author3)

shop_1 = Shop(name="Первый книжный")
shop_2 = Shop(name="Второй книжный")
shop_3 = Shop(name="Третий книжный")

stock1 = Stock(count=1, book=book_1_author1, shop=shop_3)
stock2 = Stock(count=1, book=book_2_author1, shop=shop_3)
stock3 = Stock(count=1, book=book_1_author2, shop=shop_2)
stock4 = Stock(count=1, book=book_2_author2, shop=shop_2)
stock5 = Stock(count=1, book=book_1_author2, shop=shop_1)
stock6 = Stock(count=1, book=book_2_author2, shop=shop_1)
stock7 = Stock(count=1, book=book_1_author3, shop=shop_1)
stock8 = Stock(count=1, book=book_2_author3, shop=shop_1)

session.add_all([
    author1, author2, author3,
    book_1_author1, book_2_author1,
    book_1_author2, book_2_author2,
    book_1_author3, book_2_author3,
    shop_1, shop_2, shop_3,
    stock1, stock2, stock3,
    stock4, stock5, stock6,
    stock7, stock8
])
session.commit()

find_shop(session, client_name="Author_1")

session.close()






