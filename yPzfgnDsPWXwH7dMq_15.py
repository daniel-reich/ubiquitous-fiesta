
class Pagination:
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 0
        self.minPage = 0
        self.maxPage = len(self.items) // self.pageSize
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        return self.pageSize
​
    def getCurrentPage(self):
        return self.currentPage + 1
​
    def getVisibleItems(self):
        offset = self.currentPage * self.pageSize
        return self.items[offset:offset + self.pageSize]
​
    def nextPage(self):
        self.currentPage = self.currentPage + 1 if self.currentPage < self.maxPage else self.maxPage
        return self
​
    def prevPage(self):
        self.currentPage = self.currentPage - 1 if self.currentPage > self.minPage else self.minPage
        return self
​
    def firstPage(self):
        self.currentPage = self.minPage
        return self
​
    def lastPage(self):
        self.currentPage = self.maxPage
        return self
​
    def goToPage(self, page):
        self.currentPage = self.minPage if int(page) < self.minPage else self.maxPage if int(page) > self.maxPage else int(page) - 1
        return self

