from bookcase import *


bc = Bookcase.create_bookcase([('book_title', 'book_author'), ('book_two_title', 'book_two_author')])

print('-'*10)
print(bc)
print(bc.books)
print(bc.books[0])
print('-'*10)
