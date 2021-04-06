
class Book:
  def __init__(self,title, author):
    self.title = title
    self.author = author
  
  def get_title(self):
    return 'Title: {}'.format(self.title)
  def get_author(self):
    return 'Author: {}'.format(self.author)
  #Write your attributes and methods here
​
PP = Book("Pride and Prejudice","Jane Austen")
H = Book("Hamlet","William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")
​
#Instantiate your Book class here

