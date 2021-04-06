
def who_goes_free(n, s):
    s -= 1
    n = [x for x in range(n)]
​
    index = 0
​
    while ( len(n) > 1 ):
        index += s
        if index >= len(n):
            index %= len(n)
        nn = []
        for x in range(len(n)):
            if not x == index:
                nn.append(n [x])
        n = nn
        
    return n [0]

