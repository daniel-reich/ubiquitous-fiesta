
def junction_or_self(n):
    listn = list(range(n, 1, -1))
    result = []
    if n < 10:
        for i in range(n+1):
            if i*2 == n:
                result.append(i)
    elif n >= 10:
        for x in listn:
            strx = str(x)
            listx = []
            for i in strx:
                listx.append(int(i))
            if sum(listx) + x == n:
                result.append(x)
    return result if len(result)>=1 else "Self"

