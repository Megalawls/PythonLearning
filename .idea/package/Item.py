class Item ():
    def __init__(self, isbn, title, author, genre, rating, stock=[]):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
        self.stock = stock

    def toString(self):
        return "Title: " + self.title + "\nAuthor: " + self.author + "\nStock: " + str(len(self.stock)) + " Items \nRating: " + str(self.rating)

class Stock ():
    def __init__(self, id, due, type, rentedTo):
        self.id = id
        self.due = due
        self.type = type
        self.rentedTo = rentedTo
