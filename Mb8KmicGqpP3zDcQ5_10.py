
from collections import defaultdict
def josephus(people, step):
    soldiers = list(range(people))
    is_alive = {i: True for i in range(people)}
    pos = 0
    while len([k for k,v in is_alive.items() if v]) > 1:
        cnt_alive = 0
        if is_alive[pos]:
            cnt_alive += 1
        while cnt_alive < step:
            pos = (pos + 1) % len(soldiers) 
            if is_alive[pos]:
                cnt_alive += 1     
        is_alive[pos] = False
    return [k for k,v in is_alive.items() if v][0] +1

