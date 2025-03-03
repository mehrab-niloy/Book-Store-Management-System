from main import load_books

def view_books():
    books=load_books()
    for book in books:
        print(f"title:{book.title} author:{book.author} isbn:{book.isbn} genre:{book.genre} price:{book.price} quantity:{book.quantity}")

def search_book():
    books=load_books()
    test=0
    isbn=input("Enter isbn: ").strip()
    for book in books:
        if isbn==book.isbn:
            print(f"title:{book.title} author:{book.author} isbn:{book.isbn} genre:{book.genre} price:{book.price} quantity:{book.quantity}")
            test=1

    if test==0:
        print("Book is not available")
        