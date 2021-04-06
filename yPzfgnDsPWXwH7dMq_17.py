
class Pagination:
    def __init__(self,x=[],y=10):
        self.items = x
        self.pageSize = y
        self.curr = [self.items[i] for i in range(self.pageSize)] if self.items != [] else [] 
        self.currpage = 1
        self.endpage = (len(self.items)//self.pageSize) + 1 if (len(self.items)%self.pageSize!=0) else (len(self.items)//self.pageSize)
​
        
    def getPageSize(self):
        return self.pageSize
    def getItems(self):
        return self.items
​
    def getVisibleItems(self):
        start = self.pageSize * self.currpage - self.pageSize
        end = min(self.pageSize * self.currpage,len(self.items))
        self.curr = [self.items[i] for i in range(start,end)]
        return self.curr
    def getCurrentPage(self):
        return self.currpage
​
    def nextPage(self):
        self.currpage += 1
        if self.currpage > self.endpage:
            self.currpage = self.endpage
        return self
    def lastPage(self):
        self.currpage = self.endpage
        return self
    def prevPage(self):
        self.currpage -= 1
        if self.currpage == 0:
            self.currpage = 1
        return self
    def firstPage(self):
        self.currpage = 1
        return self
    def goToPage(self,num):
        num = int(num)
        if num*self.pageSize > len(self.items):
            return self.lastPage()
        if num < 1:
            return self.firstPage()
        self.currpage = num
        return self

