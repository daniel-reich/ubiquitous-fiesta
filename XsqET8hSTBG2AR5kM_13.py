
def letter_distance(txt1, txt2):
    d = 0
    flag = 0
​
    if len(txt1) > len(txt2) or len(txt2) > len(txt1):
        flag = True
​
    if len(txt1) == len(txt2) or len(txt2) > len(txt1):
        N = len(txt1)
    else:
        N = len(txt2)
​
    for u in range(N):
         d += dist(ord(txt1[u]), ord(txt2[u]))
​
    if flag == 0:
        return d
    else:
        d += dist(len(txt1), len(txt2))
        return d
​
def dist(l1, l2):
    return abs(l1 - l2)

