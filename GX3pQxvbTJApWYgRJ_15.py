
def is_kaprekar(n):
    num = str(n * n)
    if len(num) == 1:
        return int(num) == n
    i = len(num)//2
    return int(num[:i]) + int(num[i:]) == n

