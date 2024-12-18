from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from conf import DATABASE_URL
from models.genre import Genre
from models.author import Author
from models.city import City
from models.book import Book
from models.client import Client
from models.buy import Buy
from models.step import Step
from models.buy_step import BuyStep
import random


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

fake = Faker()


def generate_genres(count=5):
    genres = []
    for _ in range(count):
        genre = Genre(name_genre=fake.word())
        genres.append(genre)
    session.add_all(genres)
    session.commit()
    return genres


def generate_authors(count=10):
    authors = []
    for _ in range(count):
        author = Author(name_author=fake.name())
        authors.append(author)
    session.add_all(authors)
    session.commit()
    return authors


def generate_cities(count=5):
    cities = []
    for _ in range(count):
        city = City(name_city=fake.city(), days_delivery=random.randint(1, 10))
        cities.append(city)
    session.add_all(cities)
    session.commit()
    return cities


def generate_books(authors, genres, cities, count=20):
    books = []
    for _ in range(count):
        book = Book(
            title=fake.catch_phrase(),
            author_id=random.choice(authors).author_id,
            genre_id=random.choice(genres).genre_id,
            city_id=random.choice(cities).city_id,
            price=random.randint(10, 100),
            amount=random.randint(1, 100),
        )
        books.append(book)
    session.add_all(books)
    session.commit()
    return books


def generate_clients(count=10):
    clients = []
    for _ in range(count):
        client = Client(name_client=fake.name(), email=fake.email())
        clients.append(client)
    session.add_all(clients)
    session.commit()
    return clients


def generate_buys(clients, books, count=15):
    buys = []
    for _ in range(count):
        buy = Buy(
            client_id=random.choice(clients).client_id,
            book_id=random.choice(books).book_id,
            amount=random.randint(1, 5),
        )
        buys.append(buy)
    session.add_all(buys)
    session.commit()
    return buys


def generate_steps(count=5):
    steps = []
    for _ in range(count):
        step = Step(name_step=fake.word())
        steps.append(step)
    session.add_all(steps)
    session.commit()
    return steps


def generate_buy_steps(buys, steps):
    buy_steps = []
    for buy in buys:
        for step in steps:
            buy_step = BuyStep(
                buy_id=buy.buy_id,
                step_id=step.step_id,
                date_step_beg=fake.date_this_year(),
                date_step_end=fake.date_this_year(),
            )
            buy_steps.append(buy_step)
    session.add_all(buy_steps)
    session.commit()
    return buy_steps


def run():
    genres = generate_genres()
    authors = generate_authors()
    cities = generate_cities()
    books = generate_books(authors, genres, cities)
    clients = generate_clients()
    buys = generate_buys(clients, books)
    steps = generate_steps()
    generate_buy_steps(buys, steps)
