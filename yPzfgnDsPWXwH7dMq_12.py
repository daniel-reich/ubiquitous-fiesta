
class Pagination:
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = int(round(len(items)/pageSize+0.4999))
        self.currentPage = 1
​
    def getItems(self):
        return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage
​
    def prevPage(self):
        if self.currentPage>1:
            self.currentPage -= 1
        return self
​
    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
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
        if page > self.totalPages:
            self.currentPage = self.totalPages
        elif page > 0:
            self.currentPage = int(page)
        else:
            self.currentPage = 1
        return self
​
    def getVisibleItems(self):
        inicio = (self.getCurrentPage()-1) * self.getPageSize()
        fim = inicio + self.getPageSize()
        if self.getCurrentPage() == self.totalPages:
            return self.getItems()[inicio:]
        return self.getItems()[inicio:fim]

