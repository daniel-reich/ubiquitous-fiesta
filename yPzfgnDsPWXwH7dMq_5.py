
import math
class Pagination:
​
    def __init__(self, items=0, pageSize=10):
        self.items = items
        if type(items) != list:
          items = [items]
        self.pageSize = pageSize
        self.totalPages = math.ceil(len(items) / pageSize)
        self.currentPage = 1
        self.itemsPerPage = math.ceil(len(items)/self.totalPages)
        
    def getItems(self):
        return self.items
​
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
        if self.currentPage != self.totalPages:
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
        page = math.floor(page)
        if page > self.totalPages:
          self.currentPage = self.totalPages
        elif page < 1:
          self.currentPage = 1
        else:
          self.currentPage = page
        return self
    # Returns the currently visible items as an array
    def getVisibleItems(self):
        max = (((self.currentPage-1) * self.pageSize) + self.pageSize)
        if max > len(self.items):
          max = len(self.items)
        return [self.items[i] for i in range(((self.currentPage-1) * self.pageSize) , max) ]

