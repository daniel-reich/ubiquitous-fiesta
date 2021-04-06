
class Pagination:
    page_number = 0
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = divmod(len(items), pageSize)[0] if not divmod(
            len(items), pageSize)[1] else divmod(len(items), pageSize)[0] + 1
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
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            return self
        return self
​
    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage += 1
            return self
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
    def goToPage(self, page_number):
        self.page_number = int(page_number)
        if self.page_number >= self.totalPages:
            self.currentPage = self.totalPages
            return self
        elif self.page_number <= 2:
            self.currentPage = 1
            return self
        else:
            self.currentPage = self.page_number
            return self
​
    def getVisibleItems(self):
        self.page = []
        self.pages = []
        for self.item in self.items:
            if len(self.page) < self.pageSize:
                self.page.append(self.item)
            else:
                self.pages.append(self.page)
                self.page = []
                self.page.append(self.item)
        self.pages += [self.page]
        return self.pages[self.currentPage - 1]

