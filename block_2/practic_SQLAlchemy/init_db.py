from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import generate_data
from conf import DATABASE_URL
from models.base import Base
from models.genre import Genre
from models.author import Author
from models.city import City
from models.book import Book
from models.client import Client
from models.buy import Buy
from models.step import Step
from models.buy_step import BuyStep


# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL)


def drop_all_tables():
    Base.metadata.drop_all(engine)
    print("Все таблицы удалены.")


def init_db():
    Base.metadata.create_all(engine)
    print("База данных и таблицы успешно созданы!")


# Основной скрипт
if __name__ == "__main__":
    print("Начинаем настройку базы данных...")
    drop_all_tables()
    init_db()
    print("Данные успешно сгенерированы и добавлены в базу данных!")
    generate_data.run()
    print("Настройка базы данных завершена.")
