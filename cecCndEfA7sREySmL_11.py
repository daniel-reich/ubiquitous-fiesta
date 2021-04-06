
def challenge1(s):
    return s[:5]
​
def challenge2(s):
    return s[-5:]
​
def challenge3(s):
    return s[::-1]
​
def challenge4(s):
    return s[::-1][-6:]
​
def challenge5(s):
    return ''.join(l for idx, l in enumerate(s[-7:]) if not idx % 2)

