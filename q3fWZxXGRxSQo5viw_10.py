
import math
​
def cal(cm):
    if cm < 150:
        return math.ceil(cm/5)
    if 0<=cm % 120 <=30:
        return (cm //120-1)*40 + math.ceil( (cm % 120 + 120)/5)
    else:
        return (cm // 120)*40 + math.ceil((cm % 120)/5)

