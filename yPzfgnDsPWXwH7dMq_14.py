
from math import ceil
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = int(pageSize)
    self.totalPages = ceil(len(items)/self.pageSize)
    self.currentPage = 0
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage+1
    
  # Goes to the previous page
  def prevPage(self):
    self.currentPage=max(0,self.currentPage-1)
    return self
    
  # Goes to the next page
  def nextPage(self):
    self.currentPage=min(self.totalPages-1,self.currentPage+1)
    return self
    
  # Goes to the first page
  def firstPage(self):
    self.currentPage=0
    return self
    
  # Goes to the last page
  def lastPage(self):
    self.currentPage=self.totalPages-1
    return self
    
  # Goes to a page determined by the `page` argument
  def goToPage(self,p):
    p=int(p)
    if p>self.totalPages:
      p=self.totalPages
    elif p<1:
      p=1
    self.currentPage=p-1  
      
    return self
    
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    p=self.currentPage
    s=self.pageSize
    if p!=self.totalPages-1:
      return self.items[p*s:(p+1)*s]
    else:
      return self.items[p*s:]

