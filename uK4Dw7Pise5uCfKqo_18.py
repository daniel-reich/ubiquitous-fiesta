
class Book:
​
  def __init__(self, title, author):
    self.title = title
    self.author = author
  
  def get_title(self):
    return 'Title: ' + self.title
  
  def get_author(self):
    return 'Author: ' + self.author
​
#Pride and Prejudice - Jane Austen
#Hamlet - William Shakespeare (H)
#War and Peace - Leo Tolstoy (WP)
​
PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')

