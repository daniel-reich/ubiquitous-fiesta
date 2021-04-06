
def replace(txt, r):
    result = ''
    first, last = r.split('-')
    for num in range(ord(first), ord(last)+1):
        result += chr(num)
    sol = ''
    for char in txt:
        if char in result:
            sol += '#'
        else:
            sol += char
    return sol

