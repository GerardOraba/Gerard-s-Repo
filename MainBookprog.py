from InheritBook import PrintedBook, EBook

def get_printed_book_input(label):
    print(f"\nEnter Book Details ({label})")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    pages = input("Number of Pages: ")
    return PrintedBook(title, author, isbn, pages)


def get_ebook_input(label):
    print(f"\nEnter E-Book Details ({label})")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    file_size = input("File Size (MB): ")
    return EBook(title, author, isbn, file_size)


def main():
    print(" LIBRARY MANAGEMENT SYSTEM cls")

    books = []
    books.append(get_printed_book_input("Printed Book #1"))
    books.append(get_printed_book_input("Printed Book #2"))
    books.append(get_ebook_input("E-Book #1"))
    books.append(get_ebook_input("E-Book #2"))

    print("\n=== Library Book List ===")
    for book in books:
        book.display_info()

    print("\nUpdating ISBN of the first book...")
    new_isbn = input("Enter new ISBN: ")
    books[0].set_isbn(new_isbn)

    print("\nUpdated Book Information:")
    books[0].display_info()


if __name__ == "__main__":
    main()