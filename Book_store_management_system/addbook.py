import json
import os
from book import Book
# from main import load_books,save_books


def add_book():
    from main import load_books,save_books
    
    books=load_books()
    
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN/Book ID: ").strip()
    genre = input("Enter genre: ").strip()
    price = input("Enter price: ").strip()
    quantity = input("Enter quantity in stock: ").strip()
    
    if not title or not author or not isbn or not genre:
        print("Error: Title, author, ISBN, and genre are required.")
        return
    
    try:
        price=float(price)
        if price<=0:
            raise ValueError("price must be positive number")
        quantity=int(quantity)
        if quantity<=0:
            raise ValueError("quantity must be positive Integer")
        
    except ValueError as e:
        print(f"Error: {e}")
        return
    for book in books:
        if book.isbn==isbn:
             print("Error: A book with this ISBN already exists.")
             return
        
    new_book = Book(title, author, isbn, genre, price, quantity)
    books.append(new_book)
    save_books(books)


    

 
    

    


