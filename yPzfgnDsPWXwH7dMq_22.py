
class Pagination:
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = (len(items) // pageSize) + int(len(items) % pageSize != 0) + int(len(items) == 0)
    self.currentPage = 1
  
  def getItems(self):
    return self.items
  
  def getPageSize(self):
    return self.pageSize
  
  def getCurrentPage(self):
    return self.currentPage
​
  def prevPage(self):
    self.currentPage = max([1, self.currentPage - 1])
    return self
​
  def nextPage(self):
    self.currentPage = min([self.currentPage + 1, self.totalPages]) 
    return self
​
  def firstPage(self):
    self.currentPage = 1
    return self
​
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
​
  def goToPage(self, page):
    self.currentPage = max(1, min(int(page), self.totalPages))
    return self
​
  def getVisibleItems(self):
    j = self.currentPage
    k = self.pageSize
    v = (j - 1) * k
    s = self.items[v:v + k]
    return s

