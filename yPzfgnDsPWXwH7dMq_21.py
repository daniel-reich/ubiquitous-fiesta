
import math
​
class Pagination():
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.startPos = 0
        self.endPos = pageSize
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        return self.pageSize
​
    def getCurrentPage(self):
        return(math.ceil(self.endPos / self.pageSize))
​
    def getVisibleItems(self):
        return self.items[self.startPos:self.endPos]
​
    def prevPage(self):
        if self.startPos >= self.pageSize:
            self.endPos = self.endPos - self.pageSize
            self.startPos = self.startPos - self.pageSize
        return self
​
    def nextPage(self):
        if self.endPos <= len(self.items) - self.pageSize:
            self.endPos = self.endPos + self.pageSize
            self.startPos = self.startPos + self.pageSize
        elif self.endPos <= len(self.items):
            self.endPos = len(self.items)
            self.startPos = len(self.items) - len(self.items) % self.pageSize
        return self
​
    def firstPage(self):
        self.startPos = 0
        self.endPos = 3
        return self
​
    def lastPage(self):
        self.startPos = (len(self.items)) - (len(self.items) % self.pageSize)
        self.endPos = len(self.items)
        return self
​
    def goToPage(self, page):
        if page >= 1 and page <= int(len(self.items) / self.pageSize) + 1:
            self.startPos = int(page) * self.pageSize - self.pageSize
            self.endPos = int(page) * self.pageSize
        elif page > int(len(self.items) / self.pageSize) + 1:
            self.lastPage()
        elif page < 1:
            self.firstPage()
        return self

