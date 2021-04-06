
def is_kaprekar(n):
    k = n ** 2
    l = len(str(k))
    l2 = int(l / 2)
    if n == 1 or n == 0:
        return True
    elif l == 1:
        return False
​
    elif l % 2 == 0:
        return int(str(k)[l2:]) + int(str(k)[:l2]) == n
    else:
​
        return int(str(k)[l2:]) + int(str(k)[:l2]) == n

