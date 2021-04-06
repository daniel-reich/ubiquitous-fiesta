
def camel_to_snake(s):
    for i in s:
        if i.isupper():
            s = s.replace(i, '_'+i.lower())
    return s

