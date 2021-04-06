
class Minecart:
    def __init__(self, ln):
        self.v = 0
        self.index = 0
        self.result = 0
        self.len = ln
​
    def add_speed(self, speed):
        print(speed)
        if (self.result == 0 ):  
            if(self.v > 0 or self.index == 0):
                self.index += 1
                if ( self.v <= 8):
                    if (self.v + speed >= 8):
                        self.v = 8
                    elif (self.v + speed <= 0 and self.index != self.len):
                        self.v = 0
                        self.result = self.index
                    elif(self.index == self.len):
                        self.result = 0
                    else:
                        self.v += speed 
            else:
                self.result = self.index
​
    def checkResult(self):
        if (self.result == 0):
            return True
        else:
            return self.result - 1
​
def mine_run(tracks):
    rules = {"-->": +2.67, "<-->": 0, "<--": -2.67, "---": -1}
    new_Mine = Minecart(len(tracks))
    for n in tracks:
        new_Mine.add_speed(rules[n])
    return new_Mine.checkResult()

