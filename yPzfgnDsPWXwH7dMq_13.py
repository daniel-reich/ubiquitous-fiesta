
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = len([items[i:pageSize] for i in range(0,len(items),pageSize)])
    self.currentPage = 1
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage
    
  # Goes to the previous page
  def prevPage(self):
    if self.currentPage > 1:
      self.currentPage -= 1
    return self
    
  # Goes to the next page
  def nextPage(self):
    if self.currentPage < self.totalPages:
      self.currentPage += 1
    return self
    
  # Goes to the first page
  def firstPage(self):
    self.currentPage = 1
    return self
    
  # Goes to the last page
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
    
  # Goes to a page determined by the `page` argument
  def goToPage(self,page):
    if int(page) < 1:
      self.currentPage = 1
    elif int(page) > self.totalPages:
      self.currentPage = self.totalPages
    else:
      self.currentPage = int(page)
    return self
    
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    pageLst = [self.items[i:i+self.pageSize] for i in range(0,len(self.items),self.pageSize)]
    return pageLst[self.currentPage-1]

