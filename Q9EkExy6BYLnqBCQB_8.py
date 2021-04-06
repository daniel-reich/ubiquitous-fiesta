
def wrap_around(string, offset):
    if len(string) < offset: 
        offset = offset%len(string)
    elif offset < -len(string) < 0: 
        offset = -((-offset)%len(string))
    return string[offset:]+string[:offset]

