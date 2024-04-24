import requests
from ..utils.utilities import (
    load_json_data,
    save_json_data,
)


class GoogleBooksAggregator:
    def __init__(self, api_key, genres_path):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/books/v1/volumes"
        self.genres = load_json_data(genres_path)

    def fetch_books(self, query):
        params = {
            "key": self.api_key,
            "q": query,
            "maxResults": 1,
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def transform_book_data(self, items):
        books = []
        authors = set()
        for item in items:
            volume_info = item.get("volumeInfo", {})
            isbn_13 = None
            for identifier in volume_info.get("industryIdentifiers", []):
                if identifier["type"] == "ISBN_13":
                    isbn_13 = identifier["identifier"]
                    break

            book = {
                "title": volume_info.get("title"),
                "authors": volume_info.get("authors", []),
                "publishedDate": volume_info.get("publishedDate"),
                "isbn": isbn_13,
            }
            books.append(book)
            authors.update(book["authors"])
        return books, authors

    def download_books_by_genre(self) -> list:
        genre_queries = []
        for genre in self.genres:
            genre_queries.append("subject:" + genre)

        all_books = []
        for query in genre_queries:
            response = self.fetch_books(query)
            books, _ = self.transform_book_data(response.get("items", []))
            all_books.extend(books)
        return all_books

    def download_authors_by_genre(self) -> set:
        genre_queries = []
        for genre in self.genres:
            genre_queries.append("subject:" + genre)

        all_authors = set()
        for query in genre_queries:
            response = self.fetch_books(query)
            _, authors = self.transform_book_data(response.get("items", []))
            all_authors.update(authors)
        return all_authors

    def download_and_save_books(self, output_path):
        books = self.download_books_by_genre()
        save_json_data(books, output_path)

    def download_and_save_authors(self, output_path):
        authors = self.download_authors_by_genre()
        save_json_data(list(authors), output_path)
