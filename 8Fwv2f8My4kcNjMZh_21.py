
class ones_threes_nines:
    def __init__(self, x):
        self.nines = x // 9
        self.threes = (x - self.nines * 9) // 3
        self.ones = x - self.nines * 9 - self.threes * 3
        self.answer = 'nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones)

