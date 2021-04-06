
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = int(len(items) / pageSize) + 1
    self.currentPage = 1
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
  def getCurrentPage(self):
    return self.currentPage
    
  # Goes to the previous page
  def prevPage(self):
    if self.currentPage - 1 < 1:
      self.currentPage = 1
    else:
      self.currentPage -= 1
    return self
  # Goes to the next page
  def nextPage(self):
    if self.currentPage + 1 > self.totalPages:
      print(self.currentPage, self.totalPages)
      self.currentPage = self.totalPages
    else:
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
  def goToPage(self, page):
    page = int(page)
    if page in range(1, self.totalPages + 1):
      self.currentPage = page
    elif page < 1:
      self.currentPage = 1
    else:
      self.currentPage = self.totalPages
    return self
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    
    page = self.currentPage
    
    pages = {}
    n = 1
    c = 0
    p = []
    
    for item in self.items:
      if c < self.pageSize:
        p.append(item)
        c += 1
      elif c == self.pageSize:
        pages[n] = p
        n += 1
        c = 1
        p = [item]
      else:
        return 'ERROR: ' + item + ', ' + c
    
    if p != []:
      pages[n] = p
      
    return pages[page]

