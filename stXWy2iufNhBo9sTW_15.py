
def rondo():
    i = 0
    while True:
        yield "A"
        yield chr(i + 66)
        i += 1
​
​
def valid_rondo(s):
    x = rondo()
    return all(i == next(x) for i in s) & s.endswith("A") and "B" in s

