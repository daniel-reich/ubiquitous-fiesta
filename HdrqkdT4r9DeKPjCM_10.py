
import math
​
BIG = 65536
polygonal = {}
for k in range(3, BIG+1):
    polygonal[k] = [1]
    n = 1
    while True:
        C = k * n * (n + 1) // 2 + 1
        if C > BIG:
            break
        polygonal[k].append(C)
        n += 1
        
def get_postfix(k):
    if k in [11, 12, 13]:
        return "th"
    if k % 10 == 1:
        return "st"
    if k % 10 == 2:
        return "nd"
    if k % 10 == 3:
        return "rd"
    return "th"    
​
def is_square(k):
    r = int(math.sqrt(k))
    return r**2 == k
​
def is_polygonal(n):
    if n == 1:
        return "0th of all"
    if n in [2, 3]:
        return False
    if n < 10:
        return ["1st " + str(n - 1) + "-gonal number"]
    ans = []
    for k in range(3, n):
        if n in polygonal[k]:
            idx = polygonal[k].index(n)
            ans.append(str(idx) + get_postfix(idx) + " " + str(k) + "-gonal number")
    return False if len(ans) == 0 else ans

