
def spiral_order(m):
    s = []
​
    def empty(m):
        try:
            x = m [0]
            return False
        except:
            return True
        
    while not empty(m):
        for x in range(len(m [0])):
            s.append(m [0][x])
        m.pop(0)
        if not empty(m):
            for x in range(len(m)):
                s.append(m [x][len(m [x])-1])
                m [x].pop(len(m [x])-1)
​
            if not empty(m):
​
                for x in reversed(range(len(m [len(m)-1]))):
                    s.append(m [len(m)-1][x])
                m.pop(len(m)-1)
​
                if not empty(m):
​
                    for x in reversed(range(len(m))):
                        s.append(m [x][0])
                        m [x].pop(0)
​
    return s

