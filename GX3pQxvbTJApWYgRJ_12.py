
def is_kaprekar(n):
    s = str(n**2)
    if len(s)==1:  s= "0"+s
    return n == int(s[:len(s)//2]) + int(s[len(s)//2:])

