
def wrap_around(string, offset):
    offset = offset%len(string)
    return string[offset:]+string[:offset]

