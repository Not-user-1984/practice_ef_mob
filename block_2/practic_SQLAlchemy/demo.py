from db import DatabaseSession
from models.genre import Genre
from models.author import Author
from models.city import City
from models.book import Book
from models.client import Client
from models.buy import Buy
from models.step import Step
from models.buy_step import BuyStep


def query_genres(uow):
    genres = uow.session.query(Genre).all()
    print("\nТаблица Genre:")
    for genre in genres:
        print(f"ID: {genre.genre_id}, Name: {genre.name_genre}")


def query_authors(uow):
    authors = uow.session.query(Author).all()
    print("\nТаблица Author:")
    for author in authors:
        print(f"ID: {author.author_id}, Name: {author.name_author}")


def query_cities(uow):
    cities = uow.session.query(City).all()
    print("\nТаблица City:")
    for city in cities:
        print(
            f"ID: {city.city_id}, Name: {city.name_city}, Days Delivery: {city.days_delivery}"
        )


def query_books(uow):
    books = uow.session.query(Book).all()
    print("\nТаблица Book:")
    for book in books:
        print(
            f"ID: {book.book_id}, Title: {book.title}, Author ID: {book.author_id}, Genre ID: {book.genre_id}, City ID: {book.city_id}, Price: {book.price}, Amount: {book.amount}"
        )


def query_clients(uow):
    clients = uow.session.query(Client).all()
    print("\nТаблица Client:")
    for client in clients:
        print(
            f"ID: {client.client_id}, Name: {client.name_client}, Email: {client.email}"
        )


def query_buys(uow):
    buys = uow.session.query(Buy).all()
    print("\nТаблица Buy:")
    for buy in buys:
        print(
            f"ID: {buy.buy_id}, Client ID: {buy.client_id}, Book ID: {buy.book_id}, Amount: {buy.amount}"
        )


def query_steps(uow):
    steps = uow.session.query(Step).all()
    print("\nТаблица Step:")
    for step in steps:
        print(f"ID: {step.step_id}, Name: {step.name_step}")


def query_buy_steps(uow):
    buy_steps = uow.session.query(BuyStep).all()
    print("\nТаблица BuyStep:")
    for buy_step in buy_steps:
        print(
            f"Buy ID: {buy_step.buy_id}, Step ID: {buy_step.step_id}, Date Beg: {buy_step.date_step_beg}, Date End: {buy_step.date_step_end}"
        )


# Основной скрипт
if __name__ == "__main__":
    print("Выполнение ORM-запросов...")
    with DatabaseSession() as uow:
        query_genres(uow)
        query_authors(uow)
        query_cities(uow)
        query_books(uow)
        query_clients(uow)
        query_buys(uow)
        query_steps(uow)
        query_buy_steps(uow)
    print("\nЗапросы выполнены.")
