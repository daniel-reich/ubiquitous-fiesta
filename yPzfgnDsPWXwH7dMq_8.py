
from math import ceil
class Pagination:
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = ceil(len(items) / pageSize)
    self.currentPage = 1
  getItems = lambda self: self.items
  getPageSize = lambda self: self.pageSize
  getCurrentPage = lambda self: self.currentPage
  def prevPage(self):
    self.currentPage -= 1 if self.currentPage - 1 else 0
    return self
  def nextPage(self):
    self.currentPage += 1 if self.currentPage < self.totalPages else 0
    return self
  def firstPage(self):
    self.currentPage = 1
    return self
  def lastPage(self):
    self.currentPage = self.totalPages
    return self
  def goToPage(self, page):
    self.currentPage = 1 if page < 1 else self.totalPages if page > self.totalPages else int(page)
    return self
  getVisibleItems = lambda self: self.items[(self.currentPage - 1) * self.pageSize:self.currentPage * self.pageSize]

