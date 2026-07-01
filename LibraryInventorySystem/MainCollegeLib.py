from InheritCollegeLib import PrintedBook, EBook, save_books, load_books


def get_printed_book_input():
    print("\nEnter Printed Book Details:")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    pages = input("Number of Pages: ")
    return PrintedBook(title, author, isbn, pages)


def get_ebook_input():
    print("\nEnter E-Book Details:")
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


def add_book(books):
    print("\n--- Add Book ---")
    print("1. Printed Book")
    print("2. E-Book")
    choice = input("Choose the type of book (1 or 2): ")

    if choice == "1":
        book = get_printed_book_input()
    elif choice == "2":
        book = get_ebook_input()
    else:
        print("Invalid choice. No book was added.")
        return

    books.append(book)
    save_books(books)  # Save to JSON immediately after adding
    print("\nBook successfully added and saved!")


def view_all_books(books):
    if not books:
        print("\nNo books in the library yet.")
        return

    sort_books_by_isbn(books)
    print("\n=== Library Book Collection (Sorted by ISBN) ===")
    for book in books:
        book.display_info()


def search_book(books):
    if not books:
        print("\nNo books in the library yet.")
        return

    sort_books_by_isbn(books)
    print("\n--- Search Book by ISBN ---")
    target_isbn = input("Enter ISBN to search: ")
    result = binary_search_by_isbn(books, target_isbn)

    if result:
        print("\nBook Found!")
        result.display_info()
    else:
        print("\nBook not found.")


def main():
    print("=== LIBRARY BOOK INVENTORY SYSTEM ===")

    # Load existing books from JSON on startup (permanent storage)
    books = load_books()
    print(f"(Loaded {len(books)} book(s) from storage.)")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by ISBN")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_all_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()