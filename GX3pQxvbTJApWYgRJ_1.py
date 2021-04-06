
def is_kaprekar(n):
    s = str(n**2).zfill(2)
    return int(s[:len(s)//2]) + int(s[len(s)//2:]) == n

