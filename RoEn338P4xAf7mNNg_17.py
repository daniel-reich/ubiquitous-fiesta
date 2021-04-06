
def shortest_path(lst):
    s, r = [], 0
    for h, i in enumerate(lst):
        for j, k in enumerate(i):
            if k != "0":
                add = [int(k), h, j]
                s.append(add)
                
    s = sorted(s, key=lambda x : x[0])
    if not s:
        return 0
    x, y = s[0][1], s[0][2]
    
    for z in range(1, len(s)):
        r += abs(x - s[z][1]) + abs(y - s[z][2])  
        x, y = s[z][1], s[z][2]
    return r

