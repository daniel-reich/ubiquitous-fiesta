
def random(lst):
    x0 = lst[0]
    tgt_x1 = lst[1]
    a, x1 = 0, 0
    mod = 2**16-1
​
    # if gcd not one, then there are multiple 'a' values and answer is
    # not obtainable. 
    if gcd(x0, mod) != 1:
        return None
​
    while True:
        x1 = (a*x0 + 1) % mod
    
        if x1 == tgt_x1:
            return(a*x1 + 1) % mod
        else:
            a += 1
​
def gcd(x,y):
    val = 0
    if x < y:
        small_num = x
    else:
        small_num = y
​
    for i in range(1, small_num+1):
        if((x % i == 0) and (y % i == 0)):
            val = i
​
    return val

