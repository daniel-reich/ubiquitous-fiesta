
def babbage(n):
    x = ''
    l = len(str(n))
    i = 0
    while x[-l:] != str(n):
        i += 1
        x = str(i**2)
​
    if n == 269696:
        if i == 99736:
            return 'Babbage was correct!'
        else:
            return 'Babbage was incorrect!'
​
    return i

