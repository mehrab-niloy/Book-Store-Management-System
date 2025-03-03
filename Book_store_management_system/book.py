class Book:
    def __init__(self, title, author, isbn, genre, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity
#convert the book object into dictionary
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "price": self.price,
            "quantity": self.quantity
        }
#convert dictionary into book object
    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["isbn"],
            data["genre"],
            data["price"],
            data["quantity"]
        )
