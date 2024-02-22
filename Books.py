from datetime import date


class Book:
    def __init__(self, title, author, publishing_year):
        self.__title = title
        self.__author = author
        self.__publishing_year = publishing_year

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_publishing_year(self):
        return self.__publishing_year

    def set_publishing_year(self, publishing_year):
        self.__publishing_year = publishing_year


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("წიგნების სია ცარიელია")
        else:
            for book in self.books:
                print(f"სათაური: {book.get_title()}, ავტორი: {book.get_author()}, გამოშვების წელი: {book.get_publishing_year()}")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if str(book.get_title()).upper() == title.upper()]
        if not found_books:
            print("ასეთი წიგნი ვერ მოიძებნა")
        else:
            for book in found_books:
                print(f"სათაური: {book.get_title()}, ავტორი: {book.get_author()}, გამოშვების წელი: {book.get_publishing_year()}")


book_manager = BookManager()

while True:
    print("\n1. დაამატე წიგნი")
    print("2. წიგნების სია")
    print("3. მოძებნე წიგნი სათაურით")
    print("4. დასრულება")

    choice = input("ჩაწერეთ ოპერაციის შესაბამისი რიცხვი: ")

    if choice == "1":
        title = input("ახალი წიგნის სათაური: ")
        author = input("ახალი წიგნის ავტორი: ")
        publishing_year = input("ახალი წიგნის გამოცემის წელი: ")
        try:
            publishing_year = int(publishing_year)
            if publishing_year > date.today().year:
                print("წიგნი არ დაემატა სიაში")
            else:
                book = Book(title, author, publishing_year)
                book_manager.add_book(book)
                print("წიგნი დაემატა სიაში")
        except ValueError:
            print("წელი უნდა იყოს რიცხვი")

    elif choice == "2":
        print("\nწიგნების სია")
        book_manager.show_books()

    elif choice == "3":
        search_title = input("ჩაწერეთ სათაური მოსაძებნად ")
        print("\nმიმდინარეობს ძიება")
        book_manager.search_book_by_title(search_title)

    elif choice == "4":
        print("მადლობ სარგებლობისათვის")
        break

    else:
        print("არასწორი ოპერაცია")
