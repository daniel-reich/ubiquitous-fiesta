
from math import ceil
​
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = ceil(len(items)/pageSize)
    self.currentPage = 0
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage + 1
    
  # Goes to the previous page
  def prevPage(self):
    if self.currentPage > 0: self.currentPage -= 1
    return self
    
  # Goes to the next page
  def nextPage(self):
    if self.currentPage < self.totalPages-1: self.currentPage += 1
    return self
    
  # Goes to the first page
  def firstPage(self):
    self.currentPage = 0
    return self
    
  # Goes to the last page
  def lastPage(self):
    self.currentPage = self.totalPages-1
    return self
    
  # Goes to a page determined by the `page` argument
  def goToPage(self, page):
    page = int(page) - 1
    self.currentPage = 0 if page < 0 else self.totalPages-1 if page >= self.totalPages else page
    return self
    
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    start = self.currentPage * self.pageSize
    return self.items[start:(start + self.pageSize)]

