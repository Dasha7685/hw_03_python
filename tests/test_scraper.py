from books_scraper.scater import scrape_books, get_book_data

book_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
book_data = get_book_data(book_url)
def test_book_data():
    assert isinstance(book_data, dict)
    assert 'title' in book_data and 'price' in book_data \
        and 'rating' in book_data and 'in_stock' in book_data \
        and 'description' in book_data
    
def test_len_books_list():
    assert len(scrape_books()) == 1000

def test_book_title_match():
    assert book_data['title'] == "A Light in the Attic"