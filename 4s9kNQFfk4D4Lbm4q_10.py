
def ABA(s):
    pattern = 'A'
    for i in range(ord(s)-65):
        pattern = pattern + chr(66+i) + pattern
    return pattern

