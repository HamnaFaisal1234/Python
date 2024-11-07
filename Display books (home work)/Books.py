class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name

    def displayBooks(self):
        print(f"We have the following books in our library:\n{self.name}")
        for book in self.booksList:
            print(book)

if __name__ == '__main__':
    books = Library(
        ['Advance Python', 'Javascript', 'CSS', 'C++ Basics', 'HTML'],
        "Books:"
    )

    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(f"\nHello {user_name}, welcome to the library. Please choose an option:")
        print("1. Display Books\n2. Quit")

        user_choice = input("Enter your choice to continue: ")

        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            print(f"Thank you for visiting the library, {user_name}. Goodbye!")
            break
        else:
            print("Please enter a valid option.")
