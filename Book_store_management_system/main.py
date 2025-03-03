import json
import os
from book import Book
from addbook import add_book
# from display_book import view_books,search_book


data_file="book.json"

# def load_book():
#     if not os.path.exists(data_file):
#         with open(data_file, "w") as f:
#             json.dump([], f)

#     with open(data_file,"r") as f:
#         data=json.load(f)
#         books=[]
#         for book in data:
#             books.append(Book.from_dict(book))
#             return books
        
# def save_book(books):
#     with open(data_file,"w") as f:
#         book_list=[]
#         for book in books:
#             book_list.append(book.to_dict())
#         json.dump(book_list,f,indent=4)


def load_books():
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            json.dump([], f)
    with open(data_file, "r") as f:
        return [Book.from_dict(book) for book in json.load(f)]

def save_books(books):
    with open(data_file, "w") as f:
        json.dump([book.to_dict() for book in books], f, indent=4)


def main():
    from display_book import view_books,search_book
    from delete_book import remove_book
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()