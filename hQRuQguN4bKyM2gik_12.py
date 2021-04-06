
def simple_check(a, b):
    minor = a
    major = b
    if a >= b:
        minor = b
        major = a
    count = 0
    while minor > 0:
        if not major % minor:
            count += 1
        major -= 1
        minor -= 1
    return count

