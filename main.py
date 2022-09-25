import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from model import create_table, Publisher, Book


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

session.add_all([
    author1,
    author2,
    author3,
    book_1_author1,
    book_2_author1,
    book_1_author2,
    book_2_author2,
    book_1_author3,
    book_2_author3
])
session.commit()

searchParams = input("Если хотите найти автора по имени введите 1,"
                     " если хотите найти автора по номеру введите 2: ")

if (searchParams == "1"):
    name = input("Введите имя: ")
    print(session.query(Publisher).filter(Publisher.name_publisher == name).all())
else:
    id = input("Введите номер: ")
    print(session.query(Publisher).filter(Publisher.id_publisher == id).all())

session.close()
