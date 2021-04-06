
class Pagination:
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = len(items) // pageSize + int(len(items) % pageSize != 0)
        self.currentPage = 1
        
    def getItems(self):
                return self.items
        
    def getPageSize(self):
                return self.pageSize
        
    def getCurrentPage(self):
                return self.currentPage
    
    def prevPage(self):
            if self.currentPage > 1:
                self.currentPage -= 1
            return self
        
    def nextPage(self):
            if self.currentPage == self.totalPages:
                pass
            else:
                self.currentPage += 1
            return self
        
    def firstPage(self):
            self.currentPage = 1
            return self
        
    def lastPage(self):
            self.currentPage = self.totalPages
            return self
        
    def goToPage(self, page):
            if int(page) > self.totalPages :
                self.currentPage = self.totalPages
            elif int(page) < 1:
                self.currentPage = 1
            else:
                self.currentPage = int(page)
            return self
        
    def getVisibleItems(self):
            start = self.pageSize * (self.currentPage - 1)
            end = self.pageSize * self.currentPage
            return self.items[start:end]

