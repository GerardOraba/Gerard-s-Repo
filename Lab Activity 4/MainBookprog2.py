from InheritBook2 import PrintedBook, EBook


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


def sort_books_by_isbn(books):
    books.sort(key=lambda book: book.get_isbn())


def binary_search_by_isbn(books, target_isbn):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_isbn = books[mid].get_isbn()

        if mid_isbn == target_isbn:
            return books[mid]
        elif mid_isbn < target_isbn:
            low = mid + 1
        else:
            high = mid - 1

    return None


def main():
    print("=== LIBRARY MANAGEMENT SYSTEM ===")

    books = []

    
    num_books = int(input("\nHow many books do you want to enter? "))

    for i in range(1, num_books + 1):
        print(f"\n--- Book #{i} ---")
        print("1. Printed Book")
        print("2. E-Book")
        choice = input("Choose the type of book (1 or 2): ")

        if choice == "1":
            books.append(get_printed_book_input(f"Printed Book #{i}"))
        elif choice == "2":
            books.append(get_ebook_input(f"E-Book #{i}"))
        else:
            print("Invalid choice. Skipping this entry.")

    
    sort_books_by_isbn(books)

    print("\n=== Library Book List (Sorted by ISBN) ===")
    for book in books:
        book.display_info()

    
    print("\n=== Search Book by ISBN ===")
    search_isbn = input("Enter ISBN to search: ")
    result = binary_search_by_isbn(books, search_isbn)

    if result:
        print("\nBook Found!")
        result.display_info()
    else:
        print("\nBook not found.")


if __name__ == "__main__":
    main()