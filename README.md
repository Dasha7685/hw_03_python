# Парсинг, Git и тестирование на Python
## Цель проекта
Данный проект предназначен для сбора и парсинга данных о книгах с сайта [Books to Scrape](http://books.toscrape.com). Результаты парсинга сохраняются в текстовом файле в папке `artifacts/` для дальнейшего анализа.
## Структура проекта
  ```
  books_scraper/
  ├── artifacts/
  │   └── books_data.txt
  ├── notebooks/
  │   └── HW_03_python_ds_2025.ipynb
  ├── scraper.py
  ├── README.md
  ├── tests/
  │   └── test_scraper.py
  ├── .gitignore
  └── requirements.txt
  ```
## Установка и запуск
1. Клонируйте репозиторий:
git clone https://github.com/Dasha7685/hw_03_python.git
2. Создайте и активируйте виртуальное окружение:
- Linux/Mac:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
3. Установите зависимости:
pip install -r requirements.txt
4. Запустите основной скрипт для парсинга данных:
python scraper.py
## Тестирование
Для запуска тестов в корне проекта используйте команду:
pytest
## Используемые библиотеки
- requests — для HTTP-запросов
- BeautifulSoup (bs4) — для парсинга HTML
- pytest — для запуска тестов
