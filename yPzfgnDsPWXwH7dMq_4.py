
class Pagination:
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = (len(items) + (pageSize - len(items)) % pageSize) // pageSize
    self.currentPage = 1
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage
    
  def prevPage(self):
    self.currentPage = max(self.currentPage - 1, 1)
    return self
    
  def nextPage(self):
    self.currentPage = min(self.currentPage + 1, self.totalPages)
    return self
    
  def firstPage(self):
    self.currentPage = 1
    return self
    
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
    
  def goToPage(self, page):
    self.currentPage = min(max(int(page), 1), self.totalPages)
    return self
    
  def getVisibleItems(self):
    start = (self.currentPage - 1) * self.pageSize
    return self.items[start:start + self.pageSize]

