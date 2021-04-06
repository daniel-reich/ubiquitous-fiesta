
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = len(items)//pageSize+1
    self.currentPage = 1
    
  def getItems(self):
    return self.items
  def getPageSize(self):
    return self.pageSize
  def getCurrentPage(self):
      return self.currentPage
  
  def prevPage(self):
    if self.currentPage>1:
      self.currentPage-=1
    return self
  
  def nextPage(self):
    if self.currentPage<(self.totalPages):
      self.currentPage+=1
    return self
​
  def firstPage(self):
    self.currentPage=1
    return self
​
  def lastPage(self):
    self.currentPage=self.totalPages
    return self
    
  def goToPage(self, page):
    page=int(page)
    if page in range (self.totalPages):
      self.currentPage=page
    elif page>self.totalPages:
      self.currentPage=self.totalPages
    else:
      self.currentPage=1
    return self
    
  def getVisibleItems(self):
    return self.items[(self.currentPage-1)*self.pageSize:self.currentPage*self.pageSize]

