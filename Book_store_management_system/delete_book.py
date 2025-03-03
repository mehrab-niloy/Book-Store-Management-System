

def remove_book():
    from main import load_books,save_books
    books=load_books()
    isbn=input("Enter isbn for delete book :")
    for book in books:
        if book.isbn==isbn:
            books.remove(book)
            save_books(books)
            return
        
    print("no books is availabe with this isbn")
