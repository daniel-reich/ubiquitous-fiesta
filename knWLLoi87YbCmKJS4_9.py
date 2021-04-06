
def happy(n):
    x = n
    while True:
        s = sum([int(i) ** 2 for i in str(x)])
        if s == 4:
            return False
        if s == 1:
            return True
        x = s

