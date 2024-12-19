import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL страницы с результатами торгов
BASE_URL = "https://spimex.com/markets/oil_products/trades/results/"

# Базовый URL для добавления к ссылкам
BASE_DOMAIN = "https://spimex.com"


# Функция для извлечения ссылок на XLS-файлы и даты торгов
def extract_xls_links_and_dates(soup):
    """
    Извлекает все ссылки на XLS-файлы и даты торгов с текущей страницы.
    """
    xls_links = []
    dates = []

    for item in soup.find_all("div", class_="accordeon-inner__item"):
        # Извлекаем ссылку на XLS-файл
        link_element = item.find("a", class_="accordeon-inner__item-title link xls")
        if link_element:
            xls_links.append(link_element["href"])
        else:
            xls_links.append(None)
        date_element = soup.select_one(
            "html body main section div div:nth-of-type(2) div div div:nth-of-type(2) div:nth-of-type(1) div div:nth-of-type(1) div:nth-of-type(5) div div:nth-of-type(2) div p span"
        )
        if date_element:
            date = date_element.text.strip()
            dates.append(date)
        else:
            dates.append(None)

    # Отладочные сообщения
    for date, link in zip(dates, xls_links):
        if date and link:
            print(f"Найдена дата: {date}, Ссылка: {link}")
        elif link:
            print(f"Ссылка: {link}, но дата не найдена")
        elif date:
            print(f"Дата: {date}, но ссылка не найдена")

    return xls_links, dates


def get_next_page_url(soup):
    """
    Извлекает ссылку на следующую страницу из пагинации.
    """
    next_page_link = soup.find("li", class_="bx-pag-next")
    if next_page_link and next_page_link.find("a"):
        return next_page_link.find("a")["href"]
    return None


# Основная функция
def save_xls_links_and_dates():
    page_url = BASE_URL
    all_links = []  # Список для хранения всех ссылок
    all_dates = []  # Список для хранения всех дат
    page_counter = 1  # Счётчик страниц

    while page_url:
        print(f"Обрабатывается страница {page_counter}...")

        # Загружаем страницу
        try:
            response = requests.get(page_url)
            response.raise_for_status()  # Проверяем, что запрос успешен
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке страницы {page_url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Извлекаем ссылки на XLS-файлы и даты торгов
        xls_links, dates = extract_xls_links_and_dates(soup)
        all_links.extend(xls_links)
        all_dates.extend(dates)

        # Проверяем даты на год
        for date in dates:
            if date:
                # Разделяем дату по точке и извлекаем год
                date_parts = date.split(".")
                if len(date_parts) >= 3:
                    year = int(date_parts[-1])  # Последний элемент - год
                    if year < 2003:
                        print(
                            f"Дата торгов {date} меньше 2003 года. Остановка парсинга."
                        )
                        break
                else:
                    print(f"Некорректный формат даты: {date}")
                    continue

        else:
            next_page_url = get_next_page_url(soup)
            if next_page_url:
                page_url = BASE_DOMAIN + next_page_url
                page_counter += 1
                time.sleep(2)  # Добавляем задержку между запросами
            else:
                print("Достигнута последняя страница.")
                break

        if year and year < 2023:
            break

    data = {
        "Дата торгов": all_dates,
        "Ссылка на скачивание": [
            BASE_DOMAIN + link if link else None for link in all_links
        ],
    }
    df = pd.DataFrame(data)

    # Убираем строки, где дата или ссылка отсутствуют
    df = df[df["Дата торгов"].notna() & df["Ссылка на скачивание"].notna()]

    # Сохраняем DataFrame в CSV-файл
    df.to_csv("trading_results.csv", index=False, encoding="utf-8")
    print(f"Данные сохранены в файл: trading_results.csv")


if __name__ == "__main__":
    save_xls_links_and_dates()
