
def player1_wins(a):
    def is_high(p1, p2):
        d = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        c1, c2 = 0, 0
        for i in range(5):
            c1 += d.get(p1[i][0]) if p1[i][0] in d else int(p1[i][0])
            c2 += d.get(p2[i][0]) if p2[i][0] in d else int(p2[i][0])
        return 'p1' if c1 > c2 else 'p2'
​
    def is_pair(p1, p2):
        d = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        cp1, cp2 = 0, 0
        cp1v, cp2v = [], []
        for i in range(5):
            for j in range(5):
                if p1[i] != p1[j] and p1[i][0] == p1[j][0]:
                    cp1 += 1
                    cp1v.append(d.get(p1[i][0]) if p1[i][0] in d else int(p1[i][0]))
                if p2[i] != p2[j] and p2[i][0] == p2[j][0]:
                    cp2 += 1
                    cp2v.append(d.get(p2[i][0]) if p2[i][0] in d else int(p2[i][0]))
​
        return 'p1' if cp1 > cp2 and sum(cp1v) > sum(cp2v) else 'p2'
​
    c = 0
    for i in a:
​
        p1, p2 = i.split(" ")[:5], i.split(' ')[5:]
​
        if is_pair(p1, p2) == 'p1':
            c += 1
            continue
        elif is_high(p1, p2) == 'p1':
            c += 1
            continue
​
    return c

