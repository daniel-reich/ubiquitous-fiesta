
def wiggle_string(s):
    i = 0
    result = []
    while i < len(s):
        result.append(" " * i + s )
        i += 1
    while i > -1:
        result.append(" " * i + s)
        i -= 1
    return result

