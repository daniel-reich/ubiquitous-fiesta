
def camel_to_snake(s):
    import string
    d = string.ascii_uppercase
    res = [x if x not in d else '_' + x.lower() for x in s]
    return ''.join(res)

