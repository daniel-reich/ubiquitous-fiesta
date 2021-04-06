
def is_kaprekar(n):
​
    if n in [0,1,9]:
        return True
    elif len(str(n)) < 2:
        return False
    else:
        d = str(n**2)
        return int(d[:len(d)//2]) + int(d[len(d)//2:]) == n

