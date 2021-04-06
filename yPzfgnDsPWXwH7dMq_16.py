
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = int(pageSize)
    self.totalPages = (len(items)+self.pageSize-1)//self.pageSize
    self.currentPage = 0
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage+1
    
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
    page = int(page)-1
    if page < 0: page = 0
    elif page >= self.totalPages: page = self.totalPages-1 
    if page >= 0 and page < self.totalPages:
      self.currentPage = page
    return self
    
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    posn = self.currentPage*self.pageSize
    return self.items[posn:posn+self.pageSize]

