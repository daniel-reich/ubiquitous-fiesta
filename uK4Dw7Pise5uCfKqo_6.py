
class Book:
  def __init__(self,t,a):
    self.title=t
    self.author=a
  def get_title(self):
    return "Title: "+self.title
  def get_author(self):
    return "Author: "+self.author 
  
PP=Book('Pride and Prejudice','Jane Austen')
H=Book('Hamlet','William Shakespeare')
WP=Book('War and Peace','Leo Tolstoy')

