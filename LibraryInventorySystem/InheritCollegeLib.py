import json
import os
from oopcollegelib import Book

DATA_FILE = "library_data.json"

# Inheritance
class PrintedBook(Book):
    def __init__(self, title, author, isbn, number_of_pages):
        super().__init__(title, author, isbn)
        self.number_of_pages = number_of_pages

    # Polymorphism (own implementation of display_info)
    def display_info(self):
        print("\n--- Printed Book Information ---")
        print(f"Title       : {self.title}")
        print(f"Author      : {self.author}")
        print(f"ISBN        : {self.get_isbn()}")
        print(f"No. of Pages: {self.number_of_pages}")

    # Convert to dictionary for JSON storage
    def to_dict(self):
        return {
            "type": "PrintedBook",
            "title": self.title,
            "author": self.author,
            "isbn": self.get_isbn(),
            "number_of_pages": self.number_of_pages
        }


class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

    # Polymorphism (own implementation of display_info)
    def display_info(self):
        print("\n--- E-Book Information ---")
        print(f"Title        : {self.title}")
        print(f"Author       : {self.author}")
        print(f"ISBN         : {self.get_isbn()}")
        print(f"File Size    : {self.file_size_mb} MB")

    # Convert to dictionary for JSON storage
    def to_dict(self):
        return {
            "type": "EBook",
            "title": self.title,
            "author": self.author,
            "isbn": self.get_isbn(),
            "file_size_mb": self.file_size_mb
        }


# Save all books to JSON file (permanent storage)
def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump([book.to_dict() for book in books], f, indent=4)


# Load all books from JSON file
def load_books():
    books = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                if item["type"] == "PrintedBook":
                    books.append(PrintedBook(
                        item["title"],
                        item["author"],
                        item["isbn"],
                        item["number_of_pages"]
                    ))
                elif item["type"] == "EBook":
                    books.append(EBook(
                        item["title"],
                        item["author"],
                        item["isbn"],
                        item["file_size_mb"]
                    ))
    return books