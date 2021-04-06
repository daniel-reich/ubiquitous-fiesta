
class Book:
  # Write your attributes and methods here
  def __init__(self, author, title):
    self.title = title
    self.author = author
  
  def get_title(self):
    return "Title: {}".format(self.title)
  
  def get_author(self):
    return "Author: {}".format(self.author)
    
  
    
  
​
  # Instantiate your Book class here
PP = Book('Jane Austen','Pride and Prejudice')
H = Book('William Shakespeare','Hamlet')
WP = Book('Leo Tolstoy','War and Peace')

