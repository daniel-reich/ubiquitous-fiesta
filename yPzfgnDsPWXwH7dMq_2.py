
import math
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = math.ceil(len(items) / pageSize)
    self.currentPage = 1
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
  
  def getCurrentPageSize(self):
    r = len(self.items) - (self.currentPage - 1) * self.pageSize
    return min(r, self.pageSize)
    
  def getCurrentPage(self):
    return self.currentPage
    
  def prevPage(self):
    return self.goToPage(self.currentPage - 1)
    
  def nextPage(self):
    return self.goToPage(self.currentPage + 1)
​
  def firstPage(self):
    return self.goToPage(1)
    
  def lastPage(self):
    return self.goToPage(self.totalPages)
    
  def goToPage(self, page):
    page = max(page, 1)
    page = min(page, self.totalPages)
    self.currentPage = int(page)
    return self
    
  def getVisibleItems(self):
    r = (self.currentPage - 1) * self.pageSize
    size = self.getCurrentPageSize()
    return self.items[r : r + size]

