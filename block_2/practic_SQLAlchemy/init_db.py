from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS
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
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Создаем все таблицы
Base.metadata.create_all(engine)

print("База данных и таблицы успешно созданы!")