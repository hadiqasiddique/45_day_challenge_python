class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been successfully added.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, query):
        found_books = [
            book for book in self.books
            if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query.lower() in book.isbn
        ]
        if not found_books:
            print("No books found.")
        else:
            for book in found_books:
                print(book)


def main():
    lib = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            lib.add_books(book)

        elif choice == "2":
            lib.view_books()

        elif choice == "3":
            query = input("Enter title, author, or ISBN to search: ")
            lib.search_books(query)

        elif choice == "4":
            print("Exiting the library application.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
