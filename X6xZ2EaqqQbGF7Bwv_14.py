
class ones_threes_nines:
    def __init__(self,num):
        self.num = num
        if self.num >= 1:
            self.ones = self.num
            self.threes = self.num // 3
        else:
            self.ones = 0
​
        if self.num >=9:
            self.nines = self.num // 9 
        else:
            self.nines = 0

