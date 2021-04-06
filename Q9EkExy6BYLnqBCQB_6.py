
def wrap_around(string, offset):
    if offset == 0:
        return string
    if offset > 0:
        offset = offset % len(string)
        return string[offset:] + string[:offset]
    else:
        offset = abs(offset) % len(string)
        return string[-offset:] + string[:-offset]

