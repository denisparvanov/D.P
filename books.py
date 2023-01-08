class Book():
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price= book_price
        self.book_year= book_year
        self.book_author = book_author
    def __repr__(self):
        return self.book_name

books = []

book_one = Book("Maika ti", 12345, 20, 2003, "Denis")
books.append(book_one)
book_two = Book("Bashta ti", 23456, 30, 20001,"Conka")
books.append(book_two)
book_three= Book("Lelq ti", 56789,40,2002,"Kondio")
books.append(book_three) 

def sort_name(books):
    books.sort(reverse = True, key= lambda elem:elem.book_name)
    print(books)
def author(searched_author, books):
    for i in books:
        if i.book_author == searched_author:
            print(i.book_name)
def search_book(searched_code, books):
    is_here = False
    for elem in books:
        if elem.book_code == searched_code:
            is_here =True
            print(elem.book_year)
    if not is_here:
        print("The book is not found !")
sort_name(books)
author("Denis", books)
search_book(12345, books)
