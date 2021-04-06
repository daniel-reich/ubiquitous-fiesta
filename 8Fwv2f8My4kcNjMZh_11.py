
class ones_threes_nines:
​
    def __init__(self, number):
        self.number = number
        self.nines = (number // 9)
        self.threes = ((number - (self.nines)*(9)) // (3))
        self.ones = (number - (self.nines)*(9) - (self.threes)*(3))
        self.answer = 'nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones)
​
    def __repr__(self):
        return self.answer

