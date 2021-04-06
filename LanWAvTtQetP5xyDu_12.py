
from collections import Counter
def coins_div(lst):
    if sum(lst) % 3: return False
    target = sum(lst) // 3
    coins = []
    subsss = [lst[x:y] for x in range(len(lst)) for y in range(x+1, len(lst)+1)]
    
    for x in subsss:
        if sum(x) == target and all(c <= Counter(lst)[k] for k, c in Counter(x).items()):
            coins.append(x)
            for coin in x:
                lst.remove(coin)
    
    if len(coins)  == 3:
        return True
​
    subs  = [[lst[y] for y in range(len(lst)) if x & 1 << y] for x in range(1, 2**len(lst))]
    
​
    for x in subs:
        if sum(x) == target and all(c <= Counter(lst)[k] for k, c in Counter(x).items()):
            coins.append(x)
            for coin in x:
                lst.remove(coin)
    return len(coins) == 3

