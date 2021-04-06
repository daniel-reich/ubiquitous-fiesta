
class Minecart:
​
    def __init__(self, v=0):
        self.v = v
​
        if self.v <= 0:
            self.im = False
        else:
            self.im = True
​
    def add_speed(self, speed):
​
        if self.im == False:
            self.im = True
​
        if self.v + speed <= 8 and self.v + speed > 0:
            self.v += speed
        elif self.v + speed <= 0:
            self.v = 0
            self.im = False
        else:
            self.v = 8
​
​
def mine_run(tracks):
    n = 0
    d = {"-->": 2.67, "<-->": 0, "<--": -2.67, "---": 1}
    ja = Minecart(d[tracks[0]])
    for i in tracks[1::]:
        n += 1
        if (len(tracks) - 1) == n:
            return True
        if i in d.keys():
            ja.add_speed(d[i])
            if ja.v <= 0:
                return n
            else:
                pass
    else:
        return True

