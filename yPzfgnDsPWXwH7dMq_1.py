
import math
​
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = math.ceil(len(items)/pageSize)
    self.currentPage = 1
​
  def getItems(self):
    return 0
    
  def getPageSize(self):
    return self.pageSize
  
  def getCurrentPage(self):
    return self.currentPage
  
  def prevPage(self):
    self.currentPage = max(1, self.currentPage - 1)
    return self
    
  def nextPage(self):
    self.currentPage = min(self.totalPages, self.currentPage + 1)
    return self
  
  def firstPage(self):
    self.currentPage = 1
    return self
    
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
    
  def goToPage(self, page):
    self.currentPage = max(1, min(self.totalPages, int(page)))
    return self
    
  def getVisibleItems(self):
    f =   (self.currentPage - 1)  * self.pageSize
    t = min((self.currentPage    )  * self.pageSize, len(self.items))
    return self.items[f:t]

