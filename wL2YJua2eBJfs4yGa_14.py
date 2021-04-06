
bab = {269696: "correct"}
​
def babbage(n):
    start = 1 if n % 2 == 1 else 2
    mod = 10**len(str(n))
    cur = start
    square = cur**2
    while square % mod != n:
        cur += 2
        square = cur**2
    return cur if n != 269696 else "Babbage was " + bab.get(cur, "incorrect") + "!"

