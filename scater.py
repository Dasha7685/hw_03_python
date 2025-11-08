import requests
import re
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_book_data(book_url: str) -> dict:
    """
    Извлекает данные о книге с ее страницы.
    Args:
        book_url (str): Ссылка на страницу книги.
    Returns:
        dict: Словарь с характеристиками книги (название, цена, рейтинг, описание и пр.)
    """

    # НАЧАЛО ВАШЕГО РЕШЕНИЯ
    response = requests.get(book_url)
    response.encoding = "utf-8"
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1").get_text()
        price = soup.find("p", attrs={"class": "price_color"}).get_text()
        re_star_rating = re.compile(r"star-rating \w+")
        star_rating = soup.find("p", attrs={"class": re_star_rating})["class"][1]
        available_str = soup.find("p", attrs={"class": "instock availability"}).get_text().strip()
        available_number = re.search(r"\d+", available_str).group(0)
        desc_tag = soup.find(lambda teg: teg.name == "p" and not teg.attrs)
        description = desc_tag.get_text() if desc_tag else ""
        product_information = {}
        table = soup.find("table")
        for row in table.find_all("tr"):
            key = row.find("th").get_text()
            value = row.find("td").get_text()
            product_information[key] = value
    return {
        'title': title,
        'price': price,
        'rating': star_rating,
        'in_stock': available_number,
        'description': description,
        **product_information
    }
    # КОНЕЦ ВАШЕГО РЕШЕНИЯ

def process_book(book_link: str) -> dict:
    """
    Получает подробные данные о книге, создав полный URL-адрес.
    Args:
        book_link (str): Частичная ссылка на книгу по ключу "href".
    Returns:
        dict: Подробные данные о книге, полученные из функции get_book_data.
    """
    book_url = f"http://books.toscrape.com/catalogue/{book_link["href"]}"
    return get_book_data(book_url)

def scrape_books(is_save: bool = False) -> list:
    """
    Собирает информацию о всех книгах каталога.
    Args:
        is_save (bool): Сохранять ли результаты в файл books_data.txt.
    Returns:
        list: Список словарей с параметрами книг.
    """

    # НАЧАЛО ВАШЕГО РЕШЕНИЯ
    all_books = []
    n = 1
    while True:
        page_url = f"http://books.toscrape.com/catalogue/page-{n}.html"
        response = requests.get(page_url)
        if response.status_code == 404:
            break
        soup = BeautifulSoup(response.text, "html.parser")
        books_on_one_page = soup.find_all("h3")
        book_links = [book.find("a") for book in books_on_one_page]
        with ThreadPoolExecutor(max_workers=10) as executor:
            all_books.extend(list(executor.map(process_book, book_links)))
        n += 1
        if is_save:
            with open("../artifacts/books_data.txt", "w", encoding="utf-8") as file:
                json.dump(all_books, file)
    return all_books
    # КОНЕЦ ВАШЕГО РЕШЕНИЯ