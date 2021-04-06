
class Minecart:
​
    def __init__(self, v=0):
​
        self.v = v
        if self.v <= 0:
            self.im = False
        else:
            self.im = True
    
    def add_speed(self,speed):
​
        if self.im == False:
            self.im = True
        if self.v + speed <= 8 and self.v + speed > 0:
            self.v += speed
        elif self.v + speed <= 0:
            self.v = 0
            self.im = False
        else:
            self.v = 8
    
    def red_speed(self,speed):
        if self.v - speed > 0 and self.v - speed < 8:
            self.v -= speed
           
        elif self.v - speed > 8:
            self.v = 8
        else:
            self.v = 0
            self.im = False
​
def mine_run(tracks):
​
    cart=Minecart()
    pos = 0
​
    for _ in tracks:
        if _ == '-->':
            cart.add_speed(2.67)
            if cart.im == True: pos += 1
            else: break
        elif _ == '<-->':
            cart.add_speed(0)
            if cart.im == True: pos += 1
            else: break
        elif _ == '<--':
            cart.red_speed(2.67)
            if cart.im == True: pos += 1
            else: break
        elif _ == '---':
            cart.red_speed(1)
            if cart.im == True: pos += 1
            else: break
        
    if pos == len(tracks)-1:
        return(True)
    else:
        return(pos)

