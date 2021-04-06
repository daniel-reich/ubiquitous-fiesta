
class Pagination(object):
​
    def __init__(self, items=[], pageSize=10):
        super(Pagination, self).__init__()
        self.items = items
        self.pageSize = int(pageSize)
        #splits items into lists the length of pageSize
        self.pages = [items[x:x+self.pageSize] for x in range(0, len(items), self.pageSize)]
        self.totalPages = len(self.pages)
        self.currentPage = 1
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        if self.items == []:
            return 10
        else:
            return len(self.pages[self.currentPage-1])
​
    def getCurrentPage(self):
        return self.currentPage
​
    def prevPage(self):
        if self.currentPage == 1:
            pass
        else:
            self.currentPage -= 1
        return self
​
    def nextPage(self):
        if self.currentPage == len(self.pages):
            pass
        else:
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
    def goToPage(self, specificPage):
        if specificPage < 1:
            self.currentPage = 1
        elif specificPage > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = int(specificPage)
        return self
​
    def getVisibleItems(self):
        return self.pages[self.currentPage-1]

