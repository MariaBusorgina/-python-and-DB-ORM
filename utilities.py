from model import Publisher, Stock, Shop, Book

def find_shop(session, id_client="", client_name=""):
    if id_client:
        name_author = input("Введите имя: ")
        author = session.query(Publisher).filter(Publisher.name_publisher == name_author).all()[0]
        print(author)
        print(f"Издатель с именем {author.name_publisher} есть в магазинах: ")
        for i in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(
                Publisher.name_publisher.like(author.name_publisher)):
            print(i.name)
    if client_name:
        id_author = input("Введите номер: ")
        author = session.query(Publisher).filter(Publisher.id_publisher == id_author).all()[0]
        print(author)
        print(f"Издатель с номером {author.id_publisher} есть в магазинах: ")
        for i in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(
                Publisher.id_publisher == author.id_publisher).all():
            print(i.name)
