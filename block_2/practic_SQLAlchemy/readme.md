### README.md


## Структура проекта

```
project/
│
├── models/
│   ├── base.py
│   ├── genre.py
│   ├── author.py
│   ├── city.py
│   ├── book.py
│   ├── client.py
│   ├── buy.py
│   ├── step.py
│   └── buy_step.py
│
├── conf.py
├── db.py
├── init_db.py
├── generate_data.py
├── demo.py
├── .env
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## Установка и настройка

### 1. Установка зависимостей

Перед началом работы убедитесь, что у вас установлены все необходимые зависимости. Установите их с помощью команды:

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта и добавьте в него следующие переменные окружения:

```
DB_NAME=bookstore
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin
PGADMIN_PORT=5050
```

### 3. Запуск Docker Compose

Для запуска PostgreSQL и pgAdmin используйте Docker Compose:

```bash
docker-compose up -d
```

После запуска вы сможете получить доступ к pgAdmin через браузер по адресу:

```
http://localhost:5050
```

Используйте следующие учетные данные для входа:

- Email: `admin@example.com`
- Password: `admin`

### 4. Инициализация базы данных

Для инициализации базы данных и создания таблиц выполните следующую команду:

```bash
python init_db.py
```

Этот скрипт выполнит следующие действия:

1. Удалит все существующие таблицы.
2. Создаст таблицы в базе данных.
3. Сгенерирует тестовые данные.

### 5. Просмотр данных

```
python3 demo.py
```

## Дополнительные инструменты

### pgAdmin

pgAdmin — это веб-интерфейс для управления PostgreSQL. После запуска Docker Compose вы можете получить доступ к pgAdmin по адресу:

```
http://localhost:5050
```

Для подключения к базе данных используйте следующие параметры:

- Host name/address: `db`
- Port: `5432`
- Maintenance database: `bookstore`
- Username: `postgres`
- Password: `postgres`

## Зависимости

Проект использует следующие библиотеки:

- `SQLAlchemy`: ORM для работы с базами данных.
- `Faker`: Для генерации тестовых данных.
- `python-dotenv`: Для загрузки переменных окружения из файла `.env`.
- `psycopg2-binary`: Драйвер PostgreSQL для Python.
