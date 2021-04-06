
import math
​
​
class Pagination:
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.totalItems = len(items)
        self.pageSize = pageSize
        self.totalPages = math.ceil(self.totalItems / self.pageSize)
        self.currentPage = 1
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        return self.pageSize
​
    def getCurrentPage(self):
        return self.currentPage
​
    # Goes to the previous page
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self
​
    # Goes to the next page
    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self
​
    # Goes to the first page
    def firstPage(self):
        self.currentPage = 1
        return self
​
    # Goes to the last page
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
​
    # Goes to a page determined by the `page` argument
    def goToPage(self, page):
        page = int(page)
        if page < 1:
            self.currentPage = 1
        elif page > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = page
        return self
​
    # Returns the currently visible items as an array
    def getVisibleItems(self):
        start = (self.currentPage-1)*self.pageSize
        end = min(start+self.pageSize, self.totalItems)
        return self.items[start:end]

