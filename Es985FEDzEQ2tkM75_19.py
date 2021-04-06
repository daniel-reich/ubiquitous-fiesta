
def g(c, a, key):
    x = ord(c) - ord(a)
    y = (x + key) % 26
    return chr(ord(a) + y)
​
def f(c, key): #c:chr
    if 'a' <= c <= 'z':
        return g(c, 'a', key)
    elif 'A'<= c <= 'Z':
        return g(c, 'A', key)
    return c
​
def caesar_cipher(a, key):
    return ''.join(f(x, key) for x in a)

