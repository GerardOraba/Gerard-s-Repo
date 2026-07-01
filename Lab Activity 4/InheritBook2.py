from oopbook2 import Book

# Inheritance
class PrintedBook(Book):
    def __init__(self, title, author, isbn, number_of_pages):
        super().__init__(title, author, isbn)
        self.number_of_pages = number_of_pages

    def display_info(self):
        print("\n--- Printed Book Information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Number of Pages: {self.number_of_pages}")


class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

    def display_info(self):
        print("\n--- E-Book Information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"File Size: {self.file_size_mb} MB")