
def pad(message):
    x = 140 - len(message)
    if x == 0:
        return message
    if x % 2 == 1:
        pad = lol(x)
    else:
        pad = ' ' + lol(x-1)
    return message + pad
​
def lol(x):
    return 'l' + 'ol' * (x//2)

