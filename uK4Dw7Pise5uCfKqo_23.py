
class Book:
  #Write your attributes and methods here
  def __init__(self, book):
    book = book.split(' - ')
    self.title = book[0]
    self.author = book[1]
  def get_title(self):
    return 'Title: {}'.format(self.title)
  def get_author(self):
    return 'Author: {}'.format(self.author)
​
#Instantiate your Book class here
HP = Book('Harry Potter - J.K. Rowling')
PP = Book('Pride and Prejudice - Jane Austen')
H  = Book('Hamlet - William Shakespeare')
WP = Book('War and Peace - Leo Tolstoy')

