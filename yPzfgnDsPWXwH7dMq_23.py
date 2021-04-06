
class Pagination:
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.lastPageN = (len(items) + pageSize - 1) // pageSize - 1
    self.currentPage = 0
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage + 1
    
  def prevPage(self):
    if self.currentPage > 0:
      self.currentPage -= 1
    return self
​
  def nextPage(self):
    if self.currentPage < self.lastPageN:
      self.currentPage += 1
    return self
    
  def firstPage(self):
    self.currentPage = 0    
    return self
​
  def lastPage(self):
    self.currentPage = self.lastPageN
    return self
    
  def goToPage(self, page):
    page = int(page) - 1
    if page > self.lastPageN:
      self.currentPage = self.lastPageN
    elif page < 0:
      self.currentPage = 0
    else:
      self.currentPage = page
    return self
    
  def getVisibleItems(self):
    return self.items[self.pageSize*self.currentPage:self.pageSize*(self.currentPage+1)]

