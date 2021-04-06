
class ones_threes_nines:
    def __init__(self, num):
        self.num = num
        self.answer = None
        if self.num <= 26:
            if self.num / 9 > 0:
                by_9 = int(self.num/9)
                if (self.num - 9*by_9)/3 > 0:
                    by_3 = int((self.num - 9*by_9)/3)
                    by_1 = (self.num - 3*by_3 - 9*by_9)
            self.answer = "nines:" + \
                str(by_9) + ", threes:" + str(by_3) + ", ones:" + str(by_1)

