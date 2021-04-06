
def lychrel(n):
    s,c = str(n),0
    while s!=s[::-1] and c<500:
        n += int(s[::-1])
        c +=1
        s = str(n)
    return c==500 or c

