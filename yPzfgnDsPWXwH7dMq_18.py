
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = int(pageSize)
    self.totalPages = len(self.items)//self.pageSize + 1
    self.currentPage = 1
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage
    
  def prevPage(self):
    if 1 < self.currentPage <= self.totalPages:
      self.currentPage -= 1 
    else:
      self.currentPage = 1
    return self
    
  def nextPage(self):
    if 1 <= self.currentPage < self.totalPages:
      self.currentPage += 1 
    else:
      self.currentPage = self.totalPages
    return self
    
  def firstPage(self):
    self.currentPage = 1
    return self
    
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
    
  def goToPage(self, page):
    page = int(page)
    if 1 <= page <= self.totalPages:
      self.currentPage = page 
    elif page < 1:
      self.currentPage = 1
    else:
      self.currentPage = self.totalPages
    return self
    
  def getVisibleItems(self):
  
    idx1 = self.currentPage * self.pageSize - self.pageSize
    
    if (idx1 + self.pageSize) < len(self.items):
      idx2 = idx1 + self.pageSize 
    else:
      idx2 = len(self.items)
      
    return self.items[idx1:idx2]

