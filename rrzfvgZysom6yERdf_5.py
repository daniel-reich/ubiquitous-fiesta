
def check_playerone(lst):
    a = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    maxes = [sorted([values.index(y[0]) for y in x]) for x in lst]
    d = {}
    for i, player in enumerate(lst):
        suits = [x[1] for x in player]
        faces = [x[0] for x in player]
        straight = any(not set(values[x:x+5]).difference(faces)for x in range(9))
        flush = len(set(suits)) == 1
        pairs = [x for x in faces if faces.count(x) == 2]
​
        if flush and not set(faces).difference(values[8:13]):
            a.append(10)
        
        elif flush and straight:
            a.append(9)
        
        elif faces.count(max(faces, key=faces.count)) == 4:
            a.append(8)
        
        elif faces.count(max(faces, key=faces.count)) == 3 and pairs:
            a.append(7)
        
        elif flush:
            a.append(6)
        
        elif straight:
            a.append(5)
        
        elif faces.count(max(faces, key=faces.count)) == 3:
            a.append(4)
        
        elif len(pairs) == 4:
            a.append(3)
        
        elif len(pairs) == 2:
            d[i] = pairs[0]
            a.append(2)
        else:
            a.append(False)
​
    # print(lst, a)
    if not a[0] and not a[1]:
        if max(maxes, key=sum) == maxes[0]:
            return True
        else:
            return False
    if a[0] == a[1]:
        if max(d[0], d[1], key=values.index) == d[0]:
            return True
    if not a[0]:
        return False
    if max(a) == a[1]:
        return False
​
    return True
​
def player1_wins(lst):
    lst = [[x.split()[:5], x.split()[5:]] for x in lst]
    p1 = 0
    
    for x in lst:
        if check_playerone(x):
            p1 += 1
​
    return p1

