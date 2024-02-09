class Quote:
    def __init__(self, author, text):
        # Ініціалізація об'єкту класу Quote з параметрами автора та тексту цитати
        self.author = author
        self.text = text

class QuoteDatabase:
    def __init__(self):
        # Ініціалізація об'єкту класу QuoteDatabase зі списком цитат
        self.quotes = []

    def add_quote(self, author, text):
        # Додавання нової цитати до бази даних
        quote = Quote(author, text)
        self.quotes.append(quote)

    def search_quotes_by_author(self, author):
        # Пошук цитат за автором
        return [quote for quote in self.quotes if quote.author == author]

    def search_quotes_by_text(self, text):
        # Пошук цитат за текстом
        return [quote for quote in self.quotes if text.lower() in quote.text.lower()]

def search_quotes(query_type, query_value, quote_db):
    # Функція для пошуку цитат за типом (автор або текст) та значенням запиту
    if query_type == "author":
        return quote_db.search_quotes_by_author(query_value)
    elif query_type == "text":
        return quote_db.search_quotes_by_text(query_value)
    else:
        # Обробка помилки, якщо передано непідтримуваний тип запиту
        raise ValueError("Неправильний тип запиту. Підтримувані типи: 'author' або 'text'")
